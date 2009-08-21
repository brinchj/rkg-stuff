#!/usr/bin/python

# constants
PS = 'data/people.dat'

# all imports
import sys, json
from Cheetah.Template import Template

# read persona template
ps = json.loads(file(PS).read())

# read, compile and print page
tmpl      = Template(file=sys.argv[2])
tmpl.ps   = ps
tmpl.name = sys.argv[1]
print unicode(tmpl).encode('utf-8')
