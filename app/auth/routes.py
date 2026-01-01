from flask import Blueprint, redirect, render_template, request, url_for


authBlueprint = Blueprint("auth",__name__)
@authBlueprint.route("/login")
def login ():
    return render_template("auth/login.html")

@authBlueprint.route("/signup",methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("auth/signup.html")
    elif request.method =='POST':
        #request.form throws an error and crashes if nothing is inputted .get returns "None"
        email = request.form.get("email")
        password = request.form.get("password")
        if email is None:
            email = ""
        if password is None:
            password = ""
        email= email.strip()
        password = password.strip()
        if email == "":
            return render_template("auth/signup.html", error="email is required")
        elif password == "": 
            return render_template("auth/signup.html", error="password is required")

        elif "@" not in email:
            return render_template("auth/signup.html", error="email must contain @")

        elif len(password) < 8:
            return render_template("auth/signup.html", error="password must be atleast 8 characters long")

        print(f"Your email is {email} and, your password is {password}")
        #send them to the dashboard mimicking a successful sign up attempt
        return redirect(url_for("dashboard.dashboard"))