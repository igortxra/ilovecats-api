import json
from datetime import datetime


def to_json(response: dict):

    return json.dumps(response).encode()


def generate_filename(prefix):
    return f"{prefix}_{datetime.now().strftime('%d-%m-%Y_%H-%m-%S')}.bmp"


def json_message(msg, title='info'):
    return to_json({title: msg})
