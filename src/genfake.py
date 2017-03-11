import json
import os
import inspect

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

data = {}
data['jobs'] = []

data['jobs'].append({
    'title': 'Director of Engineering',
    'tags': ['engineering', 'leadership', 'High Commitment'],
})
data['jobs'].append({
    'title': 'Software Engineer, R&D',
    'tags': ['engineering', 'Medium Commitment'],
})
data['jobs'].append({
    'title': 'Director of Finance',
    'tags': ['finance', 'leadership', 'High Commitment'],
})

with open(path + '/static/jobs.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
