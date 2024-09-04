
import random
import string

cache = {}

def set_value(key, value):
    err = None
    cache[key] = value
    return value, err


def get_value(key):
    err = None
    value = cache[key]
    return value, err

