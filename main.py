from flask import Flask, render_template
from database import ListJobs

app = Flask(__name__)


@app.route('/')
def index():
  JOBS = ListJobs()
  return render_template('home.html', jobs=JOBS, company_name="Baconz")


@app.route('/api/jobs')
def list_jobs():
  return ListJobs()


app.run(host='0.0.0.0', port=81, debug=True)
