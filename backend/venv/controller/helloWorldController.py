from flask import Flask, render_template, redirect, url_for #Import the class Flask
from markupsafe import escape #Import the markupsafe module to show values_iter
from flask import request #Create request with methods

app = Flask(__name__) #Create a Flask instance
# <>
@app.route('/') #Router decorator to tell flask what URL go
def index():
    return redirect(url_for('login'))

@app.route('/index')
def welcome():
    return "<h1>This is a link</h1>" #Return the message

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_login_form()

def do_the_login():
    return render_template('welcome.html')

def show_login_form():
    return render_template('form.html')

