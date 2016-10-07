#!/usr/bin/python

import datetime
import json
import sys
import shlex

date = str(datetime.datetime.now())

args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = {}
deps = []
for arg in shlex.split(args_data):

    if "=" in arg:
        (key, value) = arg.split("=")
        arguments[key] = value
        if key == "deps":
            deps = (value.split(","))

print json.dumps({
    "arguments" : arguments,
    "deps": deps,
    "changed" : True
})