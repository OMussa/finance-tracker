<<<<<<< HEAD
# app/auth/routes.py

"""
File Purpose:
    Defines all authentication-related routes (login, signup).
    These routes only return HTML templates for now.

Blueprint:
    auth_bp - handles all URLs starting with /auth
"""

from flask import Blueprint, render_template

# Create authentication blueprint
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login")
def login():
    """
    Purpose:
        Render and return the login page.

    Arguments:
        None

    Returns:
        HTML page: templates/auth/login.html

    When It's Used:
        Triggered when user goes to /auth/login
    """
    return render_template("auth/login.html")


@auth_bp.route("/signup")
def signup():
    """
    Purpose:
        Render and return the signup page.

    Arguments:
        None

    Returns:
        HTML page: templates/auth/signup.html

    When It's Used:
        Triggered when user goes to /auth/signup
    """
    return render_template("auth/signup.html")
=======
from flask import Blueprint, render_template


authBlueprint = Blueprint("auth",__name__)
@authBlueprint.route("/login")
def login ():
    return render_template("auth/login.html")

@authBlueprint.route("/signup")
def signup():
    return render_template("auth/signup.html")
>>>>>>> origin/main
