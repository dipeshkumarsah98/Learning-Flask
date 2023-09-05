
from flask import Flask,request, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/") # route defination
def welcome(): # call back function when route is called
    names = ['kesv', 'dipesh', 'karan']
    return render_template('home.html', names=names); #Things to show in route.

@app.route("/about")
def about():
    return "I'm trying "

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # getting user data from submitted login form
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        print("username:: ", username, "password:: ", password)

        if username == "admin" and password == "admin":
            return redirect(url_for('welcome'))

        return render_template('login.html')


    return render_template('login.html')

@app.route("/contact")
def contact():
    return "This is an contact page"


if __name__=="__main__":
    app.run()
