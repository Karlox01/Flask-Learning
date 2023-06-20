import os
import json # here we are importing json , So that we can import data from company.json file
from flask import Flask, render_template, request, flash # Here we are importing Flask class request is required for forms to be able to post and handle data, FLASH is used to display a message to the user once the form has been submitted, To use flash messages we need to create a secret key because flash cryptos all messages for security purposes.
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
if os.path.exists("env.py"): # This basically means if env.py file exists import it 
    import env



app = Flask(__name__) #We are than creating instance of this and storing it in a variable called app 
                      #( First argument of flask call is the name of the applications module), Since we are just using a single module we can use __name__ which is a built in python variable, 
                      #flask needs this so that it knows where to look for templates and static files
app.secret_key = os.environ.get("SECRET_KEY") # This imports secret key in order for flask to input messages without being enrcypted.

@app.route("/") #We are than using app.route decorator, In python a decorator starts with @ symbol , Effectively a decorator is a way of wrapping functions.
def index():
    return render_template("index.html")

# make sure there are two empty lines between functions to keep code pep8 compiant
@app.route('/about')
def about():
    data = []
    with open ("data/company.json", "r") as json_data: # Importing and opening data from company json file as R ( READ ) and than assigning it to variable  called json_data
        data = json.load(json_data)           # here we are assigning information we imported from company json file assigned it to json_data variable and than filtered into data list / array
    return render_template("about.html", page_title="About", company=data) # we are passing this list into return statement and will call it company




@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data: # SO how this works , We add member array to store data in it , 
        data = json.load(json_data) # storing information into data string
        for obj in data:
            if obj["url"] == member_name: # This was hard to understand, Essentially we are pairing the url to the html code if the html code is for thorin, Even if you call thorins url something else , It will still pair to HTML and display the property you want.
                member = obj
    return render_template("member.html", member=member) # first member is the html file , Second member is the member {} Array we created at the start of the function



@app.route('/contact', methods=["GET", "POST"]) # This is required in order for Flash to process the POST methods
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        sendgrid_api_key = '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'

        message = Mail(
            from_email=email,
            to_emails='kurlabol@hotmail.com',
            subject='New message from your Flask app',
            plain_text_content=f'Name: {name}\nEmail: {email}\n Phone: {phone}\nMessage: {message}'
        )
        

        try:
            # Send the email using the SendGrid API
            sg = SendGridAPIClient(os.environ.get("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"))
            response = sg.send(message)

            if response.status_code == 202:
                flash("Thank you, we have received your message.")
            else:
                flash("Failed to send email. Please try again later.")
                print("SendGrid API Error:", response.status_code)

        except Exception as e:
            flash("An error occurred while sending the email. Please try again later.")
            print("Exception:", str(e))

    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    