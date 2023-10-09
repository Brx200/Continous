#This is to import flask
from flask import Flask, render_template, request

#..

#This is where you stage ur app
app = Flask(__name__)
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        Phone_number = request.form.get('Phone_number')
        Address = request.form.get('Address')
        New_user ={'Username':Username,
                   'Password':Password,
                   'Phone number':Phone_number,
                   'Address':Address}
        print(New_user)
    return render_template("signup.html")
#..

#This is where u define ur route
@app.route('/')
def hompage():
    return render_template("Welcome.html")

    

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        New_user ={'Username':Username,
                   'Password':Password
                }
        print(New_user)
    return render_template("login.html")
#..

#This should always be the last part of this page
if __name__ == "__main__":
    app.run(debug=True)