import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import inspect
import json
import sched, time

# schedule services
jobRunner = sched.scheduler(time.time, time.sleep)
def updateJobList(jobRunnerI):
    print "Running scheduler..."
    # get directory
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    os.chdir(os.path.dirname(os.path.abspath(filename)))
    os.chdir("..")
    path = os.path.abspath(os.curdir)



    scope = ['https://spreadsheets.google.com/feeds']
    # misspelled corporate
    creds = ServiceAccountCredentials.from_json_keyfile_name(path + '/env.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Roles').sheet1

    pp = pprint.PrettyPrinter()

    wholeSheet = sheet.get_all_records()

    i = 0;
    while(i < len(wholeSheet)):
        if(wholeSheet[i]):
            if(wholeSheet[i]['Requirements']):
                wholeSheet[i]['Requirements'] = wholeSheet[i]['Requirements'].split('\n')
            if(wholeSheet[i]['Optional']):
                wholeSheet[i]['Optional'] = wholeSheet[i]['Optional'].split('\n')
        i = i+1

    jobfile = {}
    jobfile['jobs'] = wholeSheet

    with open(path + '/src/static/jobs.json', 'w') as outfile:
        json.dump(jobfile, outfile, indent=4)

    print "updated jobs"
    # do your stuff
    jobRunner.enter(120, 1, updateJobList, (jobRunnerI,))

jobRunner.enter(120, 1, updateJobList, (jobRunner,))
jobRunner.run()
