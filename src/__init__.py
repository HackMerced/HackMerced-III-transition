# do all the work here
from flask import Flask, render_template
import os
import inspect
import json
app = Flask(__name__)

# get directory
filename = inspect.getframeinfo(inspect.currentframe()).filename
os.chdir(os.path.dirname(os.path.abspath(filename)))
os.chdir("..")
path = os.path.abspath(os.curdir)



@app.route('/')
def index():
    return render_template('general/index.html')


positions = open(path + "/src/static/jobs.json", "r").read()
positions = json.loads(positions)

@app.route('/join')
def jobs():
    return render_template('general/join.html', jobs=positions )


#hello
if __name__ == "__main__":
    app.run(port=4220)
