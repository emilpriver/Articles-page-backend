import json
import sys
from pkgutil import simplegeneric


@simplegeneric
def get_items(obj):
    while False:
        yield None


@get_items.register(dict)
def _(obj):
    return obj.items()


@get_items.register(list)
def _(obj):
    return enumerate(obj)


def json_strip_whitespace(json_data):
    for key, value in get_items(json_data):
        if hasattr(value, 'strip'):
            json_data[key] = value.strip()
        else:
            json_strip_whitespace(value)
