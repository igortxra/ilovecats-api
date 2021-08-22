from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from app import *

import cgi
import json


class DefaultHandler(BaseHTTPRequestHandler):
    ''' Basic Handler for HTTP requests'''

    def get_query_string_parameter(self, qs, param_name):
        ''' Get a parameter from a query string '''

        if qs:
            alist = qs.split('&')
            qsdict = {}
            for kv in alist:
                key, value = kv.split('=')
                qsdict[key] = value
            if param_name in qsdict:
                return qsdict[param_name]
        return ''

    def setheaders(self, status=200, headers={'content-type': 'application/json'}):
        ''' Set status code and headers '''

        self.send_response(status)
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()

    def do_GET(self):
        ''' Handle GET requests '''

        parsed_url = urlparse(self.path)

        # GET /get-image
        if parsed_url.path == '/get-image':
            image_name = self.get_query_string_parameter(parsed_url.query, 'q')
            if image_name:
                headers = {
                    'content-type': 'image/bmp',
                    'content-disposition': 'attachement; filename="image.bmp"'
                }

                response = get_image(image_name)

                self.setheaders(response[0], headers)
                self.wfile.write(response[1])

        # GET /decode-message-from-image
        elif parsed_url.path == '/decode-message-from-image':
            image_name = self.get_query_string_parameter(parsed_url.query, 'q')

            response = decode_message_from_image(image_name)

            self.setheaders(response[0])
            self.wfile.write(response[1])

        # NOT FOUND
        else:
            self.send_error(404, 'Not Found')

    def do_POST(self):
        ''' Handle POST requests '''

        # POST /upload
        if self.path.endswith('/upload'):
            if self.headers['content-type']:
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                postvars = cgi.parse_multipart(self.rfile, pdict)

                response = upload_image(postvars['data'][0])

                self.setheaders(response[0])
                self.wfile.write(response[1])
            else:
                self.send_error(404, 'Not Found')

        # POST /write-message-on-image
        elif self.path.endswith('/write-message-on-image'):
            self.data_string = self.rfile.read(
                int(self.headers['Content-Length']))
            var = self.data_string.decode('utf-8')

            try:
                pdict = json.loads(self.data_string.decode('utf-8'))
            except:
                pdict = {}

            response = write_message_on_image(pdict)

            self.setheaders(response[0])
            self.wfile.write(response[1])

        # NOT FOUND
        else:
            self.send_error(404, 'Not Found')


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    ''' Run HTTP Server with the specified handler '''

    print("[RUNNING] Server listening...")
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run(handler_class=DefaultHandler)
