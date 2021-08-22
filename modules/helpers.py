import json
import random


def to_json(response: dict):
    ''' Convert a dict to json '''
    return json.dumps(response).encode()


def generate_filename(prefix):
    ''' Generate a random bmp filename'''
    code = ''.join(random.choice('cat123456789') for _ in range(3))
    return f"{prefix}_{code}.bmp"


def json_message(msg, title='info'):
    ''' Put a string on a json structure '''
    return to_json({title: msg})
