from flask import Blueprint, render_template


authBlueprint = Blueprint("auth",__name__)
@authBlueprint.route("/login")
def login ():
    return render_template("auth/login.html")

@authBlueprint.route("/signup")
def signup():
    return render_template("auth/signup.html")