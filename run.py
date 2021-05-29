from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/help")
def help():
    return "help me"

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % username

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + " + " + request.form["password"]
    else:
        return render_template('login.html')


@app.route('/aboutme', methods=['GET'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/gallery', methods=['GET'])
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
