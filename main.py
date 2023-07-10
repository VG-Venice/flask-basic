from flask import Flask, render_template, jsonify, request
from database import ListJobs, engine, loadthe_job_from_db
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    conn.execute(
      text(
        f"INSERT INTO application (job_id, full_name, email,  education, linkedin_url, work_experience, resume_url) VALUES({job_id}, '{data['full_name']}', '{data['email']}',  '{data['education']}', '{data['linkedin_url']}', '{data['work_experience']}', '{data['resume_url']}')"
      ))
  job_id = job_id

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
    return "Not found", 404
  else:
    return render_template('jobpage.html',
                           job=job,
                           company_name="Baconz Careers")


@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
  job = loadthe_job_from_db(id)
  data = request.form
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application=data,
                         company_name="Baconz Careers",
                         job=job,
                        )
  

app.run(host='0.0.0.0', port=81, debug=True)
