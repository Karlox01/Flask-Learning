import os
from flask import Flask # Here we are importing Flask class 

app = Flask(__name__) #We are than creating instance of this and storing it in a variable called app 
                      #( First argument of flask call is the name of the applications module), Since we are just using a single module we can use __name__ which is a built in python variable, 
                      #flask needs this so that it knows where to look for templates and static files


@app.route("/") #We are than using app.route decorator, In python a decorator starts with @ symbol , Effectively a decorator is a way of wrapping functions.
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    