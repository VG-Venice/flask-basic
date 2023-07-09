from flask import Flask, render_template, jsonify
from database import ListJobs, engine, loadthe_job_from_db
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    

@app.route('/')
def index():
  JOBS = ListJobs()
  return render_template('home.html', jobs=JOBS, company_name="Baconz Careers")


@app.route('/api/jobs')
def list_jobs():
  return ListJobs()

@app.route('/job/<id>')
def show_job(id):
  job = loadthe_job_from_db(id)
  if not job:
    return "Not found"
  else: 
    return render_template('jobpage.html', job=job, company_name="Baconz Careers")


app.run(host='0.0.0.0', port=81, debug=True)
