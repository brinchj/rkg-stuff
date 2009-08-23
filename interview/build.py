#!/usr/bin/python
import sys, os, re
PROCESS_DIR = r'processing/'
LATEX = r'\\includegraphics[height=\\textwidth]{images/%s.eps}\n'
print LATEX
tmpl  = file('template.tex').read()
CMDS  = ['convert images/%(name)s images/%(name)s.eps', 'latex processing/%(name)s',
         'dvips %(name)s', 'ps2pdf %(name)s.ps', 'rm -f ./%(name)s.*'] #, 'rm -f ./%(name)s.*']
for fname in os.listdir('./images'):
    file('%s/%s.tex' % (PROCESS_DIR, fname), 'w').write(re.sub('%+\s*BILLEDE', LATEX % fname, tmpl))
    # run cmds
    map(lambda cmd: os.system(cmd % {'name': fname}), CMDS)
