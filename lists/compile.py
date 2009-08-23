#!/usr/bin/python

# all imports
import sys, json
from Cheetah.Template import Template

# read persona template
ps = []
for f in sys.argv[2:]:
    ps += json.loads(file(f).read())

# read, compile and print page
tmpl      = Template(file='templates/%s.tmpl' % sys.argv[1])
tmpl.ps   = ps

print unicode(tmpl).encode('utf-8')
