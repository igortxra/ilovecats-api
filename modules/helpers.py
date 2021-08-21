import json
import random


def to_json(response: dict):

    return json.dumps(response).encode()


def generate_filename(prefix):
    code = ''.join(random.choice('cat123456789') for _ in range(3))
    return f"{prefix}_{code}.bmp"


def json_message(msg, title='info'):
    return to_json({title: msg})
