from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Brandon")
def helloBrandon():
    return "Hello Brandon!"

@app.route("/hello")
def helloTo():
    name = request.args.get('name', '')
    return "Hello {}".format(name)
    #return "Hello person!"

if __name__ == "__main__":
    app.run()