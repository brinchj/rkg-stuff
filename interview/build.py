#!/usr/bin/python
import sys, os, re
PROCESS_DIR = r'processing/'
LATEX = r'\\includegraphics[height=\\textwidth]{images/%s.eps}\n'
tmpl  = file('template.tex').read()
CMDS  = ['convert "images/%(name)s" "images/%(name)s.eps"', 'latex "processing/%(name)s"',
         'dvips "%(name)s"', 'ps2pdf "%(name)s.ps"', 'mv "%(name)s.pdf" "compiled/"',
         'rm -fv "./%(name)s."* "./processing/%(name)s."* "./images/%(name)s.eps"']
for fname in os.listdir('./images'):
    if not re.match(r'^[\w\.]+$', fname): # sanitize
        print '!! SKIPPING WEIRD FILENAME: "%s"' % fname
        print '!! PRESS ANY KEY TO CONTINUE'
        sys.stdin.readline()
        continue
    file('%s/%s.tex' % (PROCESS_DIR, fname), 'w').write(re.sub('%+\s*BILLEDE', LATEX % fname, tmpl))
    map(lambda cmd: os.system(cmd % {'name': fname}), CMDS)
