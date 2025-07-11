from flask import Flask
'''
It creates an instance of the Flask class, 
whichh will be your WSGI application
'''

# WSGI Application
app = Flask(__name__)

@app.route(rule="/")
def welcome(): 
    return "Welcome to the Flask App. This is changed"

@app.route("/index")
def index(): 
    return "Welcome to the index page"


if __name__ == "__main__": 
    app.run(debug=True)

