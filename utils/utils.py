import os
import time
from functools import wraps
from . import config
from PIL import Image
from pytesseract import image_to_string
from datetime import datetime


def path(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def dictLocator(t):
    return {"by": t[0], "value": t[1]}


def delay(secs):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            result = func(*args, **kargs)
            print("sleep " + str(secs) + " secs")
            time.sleep(secs)
            return result
        return wrapper
    return dec


class DecoMeta(type):

    def __new__(cls, name, bases, attrs):
        if config.debug:
            for attr in attrs:
                if callable(attrs[attr]) and attr.startswith("test"):
                    attrs[attr] = delay(5)(attrs[attr])
        return super(DecoMeta, cls).__new__(cls, name, bases, attrs)


def pic_to_str(file):
    import builtins
    origin_open = builtins.open

    def bin_open(file, mode='rb'):
        return origin_open(file, mode)

    try:
        builtins.open = bin_open
        image_to_bytes = image_to_string
        bs = image_to_bytes(Image.open(file), lang="chi_sim", config="-psm 6")
    finally:
        builtins.open = origin_open
    return bs.decode('utf-8')


def generate_filename(suffix='.png'):
    project_dir = path('..')
    dir = os.path.join(project_dir, 'screenshots')

    fname = datetime.now().strftime('%Y%m%d%H%M%S%f')
    return os.path.join(dir, fname + suffix)
