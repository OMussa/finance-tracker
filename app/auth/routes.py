from flask import Blueprint, redirect, render_template, request, url_for, flash,session
from app import models, extensions
from werkzeug.security import check_password_hash


authBlueprint = Blueprint("auth",__name__)
@authBlueprint.route("/login", methods = ['GET', 'POST'])
def login ():
    if request.method == "GET":
        return render_template("auth/login.html")
    elif request.method == 'POST':
        email = (request.form.get("email") or "").strip()
        password = (request.form.get("password") or "").strip()
        user = models.users.query.filter_by(email=email).first()
        if user is None or not check_password_hash(user.password_hash, password):
            flash("Either email or password is invalid","error")
            return render_template("auth/login.html")
        else:
            session["user_id"] = user.id
            flash("Successful login","success")
            return redirect(url_for("main_bp.dashboard"))
       
        


@authBlueprint.route("/signup",methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("auth/signup.html")
    elif request.method =='POST':
  
        email = (request.form.get("email") or "").strip()
        password = (request.form.get("password") or "").strip()
        existing_email= None
        if email != "" and "@" in email:
            existing_email = models.users.query.filter_by(email=email).first()
       
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
        elif existing_email:
            flash("email already exist, try again","error")
            return render_template("auth/signup.html")



        #send them to the dashboard mimicking a successful sign up attempt
        new_user = models.users(email=email)
        new_user.set_password(password)
        extensions.db.session.add(new_user)
        extensions.db.session.commit()
        flash("Signup successful!","success")
        return redirect(url_for("auth.login"))