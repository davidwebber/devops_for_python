
import random
import string

cache = {}

def set_value(key, value):
    cache[key] = value
    success = True
    return value, success


def get_value(key):
    if key in cache.keys():
        value = cache[key]
        success = True
    else:
        value = None
        success = False
    return value, success

