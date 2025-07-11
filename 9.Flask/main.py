from flask import Flask, render_template, request
'''
It creates an instance of the Flask class, 
whichh will be your WSGI application
'''

# WSGI Application
app = Flask(__name__)

@app.route(rule="/")
def welcome(): 
    return "<html><h1>Welcome to the Flask App</h1></html>"

@app.route("/index")
def index(): 
    return render_template('index.html')

@app.route('/about')
def about(): 
    return render_template('about.html')

@app.route(rule='/forms', methods=['GET', 'POST'])
def forms(): 
    if request.method == 'POST': 
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

if __name__ == "__main__": 
    app.run(debug=True)
