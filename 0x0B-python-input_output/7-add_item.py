#!/usr/bin/python3
"""Load, add, save
"""

import os
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


with open("add_item.json", 'a', encoding="utf-8") as f:
    n = len(sys.argv)
    empty = (os.stat(f.name).st_size == 0)
    if (empty):
        args = []
    else:
        args = load_from_json_file(f.name)
    for i in range(1, n):
        args.append(sys.argv[i])
    save_to_json_file(args, f.name)
