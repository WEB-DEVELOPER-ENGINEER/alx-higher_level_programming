#!/usr/bin/python3
import json
"""To JSON string
"""


def to_json_string(my_obj):
    '''
        returns the JSON representation of an object (string)
    '''
    return json.dump(my_obj)
