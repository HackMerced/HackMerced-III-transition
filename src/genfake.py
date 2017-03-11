import json

data = {}
data['jobs'] = []

data['jobs'].append({
    'title': 'Software Engineer',
    'tags': ['engineering', 'leadership', 'full time'],
})
data['jobs'].append({
    'title': 'Chief Shelley',
    'tags': ['engineering', 'leadership', 'full time'],
})

with open('./static/jobs.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
