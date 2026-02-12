from flask import Blueprint, redirect, render_template, request, url_for, flash,session
from app.auth.decorators import login_required
main = Blueprint("main_bp" ,__name__)

@main.route("/dashboard",methods = ["GET"])
@login_required
def dashboard():
    

    return render_template("main/dashboard.html")

@main.route("/history")
@login_required
def history():
    return render_template("main/history.html")