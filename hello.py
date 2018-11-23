import requests
import argparse
from flask import Flask, render_template, request

app = Flask("MyApp")

#parse argument for API key - run using python hello.py --key APIkey
parser = argparse.ArgumentParser()
parser.add_argument('--key', type=str)
args = parser.parse_args()
key = args.key

def send_simple_message(email, key):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6eaf7224c8d34fe9a5588e23922920df.mailgun.org/messages",
        auth=("api", key),
        data={"from": "Excited User <mailgun@sandbox6eaf7224c8d34fe9a5588e23922920df.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})

@app.route("/email")
def email():
    send_simple_message()
    return "Email sent"

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    firstname = form_data["firstname"]
    lastname = form_data["lastname"]
    send_simple_message(email, key)
    return "Email sent to: {} {}, {}".format(firstname, lastname, email)

app.run(debug=True)
