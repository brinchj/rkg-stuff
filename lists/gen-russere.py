#!/usr/bin/python

import json, sys

RUS = 'data/russere-all.json'
TMS = 'data/teams.json'

russ  = json.loads(file(RUS).read())
teams = json.loads(file(TMS).read())


for rus in russ:
    for t in teams:
        if rus['name'] in teams[t]:
            rus['team'] = t

print json.dumps(russ)
