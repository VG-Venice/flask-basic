from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '₹ 10,20,000'
  },
    {
    'id' : 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '₹ 11,40,000'
  },
    {
    'id' : 3,
    'title': 'Back-end Developer',
    'location': 'London, UK',
    'salary': '£ 78,000'
  },
    {
    'id' : 4,
    'title': 'Cleaner',
    'location': 'Kolkata, India',
    'salary': '₹ 3,00,000'
  }
]

@app.route('/')
def index():
    return render_template('home.html', jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
  
app.run(host='0.0.0.0', port=81, debug=True)

