from flask import Flask

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

    

@do_twice
def say_whee():
    print("Wheeeee!")

say_whee()
#do_twice(say_whee())



#from datetime import datetime

#print(datetime.now().hour)

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Hello, Carlota qué pasó!</p>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)