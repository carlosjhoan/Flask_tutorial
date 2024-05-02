from flask import Flask, render_template
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
  }
]

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name = 'CarlosJhoan')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)