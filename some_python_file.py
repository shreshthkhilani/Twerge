# From the python package flask, import the "Flask" constructor
from flask import Flask
    
# Create an app from the Flask constructor
app = Flask(__name__)
    
    
# For "/hello/world" requests, run the hello function
@app.route("/hello/world")
@app.route("/hello/world/<user>")
def hello(user=None):
    if user:
        return "<h1>Hello World, %s!<h1>" % user
    else:
        return "<h1>Hello World!<h1>"
# New app route
@app.route('/form')
def form1():
    # yes, there are better ways to do this
    return """<form action="/form-response" method="post">
                Name: <input type="text" name="name">
                Major: <input type="text" name="major">
		Year: <input type="text" name="year">
                <input type="submit" value="Send to server!">
              </form>"""
                  
# import the request library
from flask import request
    
    
@app.route('/form-response', methods=['POST'])
def recieve_form():
    print request.form['name']
    print request.form['major']
    print request.form['year']
    return "Success! <br>Check the python console for results!"    

# When file is executed, listen on the default port
if __name__ == "__main__":
    app.run()
