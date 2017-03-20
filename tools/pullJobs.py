import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import inspect
import json

# get directory
filename = inspect.getframeinfo(inspect.currentframe()).filename
os.chdir(os.path.dirname(os.path.abspath(filename)))
os.chdir("..")
path = os.path.abspath(os.curdir)

print path

scope = ['https://spreadsheets.google.com/feeds']
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

# sheet = sheet.row_values(1) to access cells across row
# sheet = sheet.col_values(1) to access cells across columns
# sheet = sheet.cell(1,1).value to access a cell at a particular index
# result = sheet.update_cell(3, 1, 'test') to update the value of the cell


# row = ["I'm", "updating", "this"]
# index = 3
# sheet.insert_row(row, index) //updating the spreadsheet with an array of strings!

# pp.pprint(result)

# result = sheet.cell(1,1).value

# pp.pprint(result)

# sheet.update_cell(1, 1, 'test')

# if lost, this is a good reference: https://www.youtube.com/watch?v=vISRn5qFrkM
