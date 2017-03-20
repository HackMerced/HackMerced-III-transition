import json
import os
import inspect



# create generic job files
filename = inspect.getframeinfo(inspect.currentframe()).filename
os.chdir(os.path.dirname(os.path.abspath(filename)))
os.chdir("..")
path = os.path.abspath(os.curdir)


# create json
jobfile = {}
jobfile['jobs'] = []

jobfile['jobs'].append({
    'title': 'Director of Engineering',
    'tags': ['engineering', 'leadership', 'High Commitment'],
})
jobfile['jobs'].append({
    'title': 'Software Engineer, R&D',
    'tags': ['engineering', 'Medium Commitment'],
})
jobfile['jobs'].append({
    'title': 'Director of Finance',
    'tags': ['finance', 'leadership', 'High Commitment'],
})

with open(path + '/src/static/jobs.json', 'w') as outfile:
    json.dump(jobfile, outfile, indent=4)

# generate env.json

envfile =  {
    "type":"service_account",
    "project_id":"your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key":"your-private-key",
    "client_email": "your-client-email",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url":"your-cert-url"
}

with open(path + '/env.json', 'w') as outfile:
    json.dump(envfile, outfile, indent=4)
