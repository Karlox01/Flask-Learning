import os
from flask import Flask, render_template # Here we are importing Flask class 

app = Flask(__name__) #We are than creating instance of this and storing it in a variable called app 
                      #( First argument of flask call is the name of the applications module), Since we are just using a single module we can use __name__ which is a built in python variable, 
                      #flask needs this so that it knows where to look for templates and static files


@app.route("/") #We are than using app.route decorator, In python a decorator starts with @ symbol , Effectively a decorator is a way of wrapping functions.
def index():
    return render_template("index.html")

# make sure there are two empty lines between functions to keep code pep8 compiant
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template("careers.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    