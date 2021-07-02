from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import abort, send_from_directory
from AzureDB import AzureDB
from datetime import datetime
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os
app = Flask(__name__)

app.secret_key = secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


github_blueprint = make_github_blueprint(
    client_id="575679c9957a89339b2a",
    client_secret="00beb8115f75849856a7481052877a5f1685fbb3"
)
app.register_blueprint(github_blueprint, url_prefix="/login")

@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return home()

@app.route('/home')
def home():
    return render_template('index.html', title='Home')


@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["emails"][0]["value"])

if __name__ == "__main__":
    app.run()

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')