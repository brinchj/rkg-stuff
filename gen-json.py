#!/usr/bin/python

import json, sys

data = file(sys.argv[1]).read()
print json.dumps([ {'name':n} for n in sorted(data.strip().split('\n')) ])
