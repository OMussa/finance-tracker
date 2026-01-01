from flask import Blueprint, redirect, render_template, request, url_for, flash


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
            flash("Email is required", "error")
            return render_template("auth/signup.html")
        
        elif "@" not in email:
            flash("email must contain '@'", "error")
            return render_template("auth/signup.html")

        elif password == "": 
            flash("Password is required", "error")
            return render_template("auth/signup.html")

        elif len(password) < 8:
            flash("Password must be at least 8 characters long", "error")
            return render_template("auth/signup.html")

        print(f"Your email is {email} and, your password is {password}")
        #send them to the dashboard mimicking a successful sign up attempt
        flash("Signup successful! Welcome aboard.","success")
        return redirect(url_for("dashboard.dashboard"))