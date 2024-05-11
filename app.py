from flask import Flask, render_template, jsonify
#from datetime import datetime

#print(datetime.now().hour)

# Jobs list
JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bangaluru, India',
    'salary': 'USD $400,000'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'USD $4,000,000'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Bogotá, Colombia',
    'salary': 'COP $4,000,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 'COP $6,000,000'
  },
  {
    'id': 5,
    'title': 'UX/UI',
    'location': 'Bucaramanga, Colombia',
  },
  {
    'id': 6,
    'title': 'Mobile Android Developer',
    'location': 'Girón, Colombia',
  },
  {
    'id': 7,
    'title': 'Administrador de base de Datos',
    'location': 'Medellín, Colombia',
    'salary': 'COP $7,000,000'
  }
]

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name = 'CarlosJhoan')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)

