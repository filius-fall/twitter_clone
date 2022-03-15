import os
from dotenv import load_dotenv


from flask import Flask,redirect,render_template,flash
from forms import RegistraionForm,LoginForm

app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.environ['FLASK_TOKEN']

@app.route("/")
def base():
    return redirect("/home")

@app.route("/home")
def home():
    nav_list = ['home','explore','notifications','messages','bookmarks','profile']
    icons = {
        'home' : 'https://img.icons8.com/ios-glyphs/30/000000/home.png',
        'explore' : 'https://img.icons8.com/material-outlined/30/000000/hashtag-2.png',
        'notifications' : '',
        'messages' : '',
        'bookmarks' : '',
    }
    user_name = "test_user_name"
    return render_template('content.html',nav_list=nav_list,user_name=user_name)

@app.route("/explore")
def explore():
    return "Explore"

@app.route("/notifications")
def notifications():
    return "Notifications"

@app.route("/messages")
def messages():
    return "Messages"

@app.route("/bookmarks")
def bookmarks():
    return "Book Marks"

@app.route("/<user_name>")
def profile(user_name):
    user_name = 'testfafda'
    profile = "testttt"
    return render_template('profile.html',user_name=user_name,profile=profile)

@app.route("/more")
def more():
    return "More"

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        return redirect('/home')
    return render_template('register.html',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sreeram@gmail.com' and form.password.data == '123456':
            return redirect('/home')
        else:
            flash('Invalid Credentials. Please try again.')
    return render_template('login.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
