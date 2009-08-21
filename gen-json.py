#!/usr/bin/python

import json

file('ps.dat','w').write(json.dumps([ {'name':n} for n in sorted(file('names.dat').read().strip().split('\n')) ]))
