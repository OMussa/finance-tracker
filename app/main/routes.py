from flask import Blueprint, render_template

main = Blueprint("main_bp" ,__name__)

@main.route("/dashboard")
def dashboard():
    return render_template("main/dashboard.html")

@main.route("/history")
def history():
    return render_template("main/history.html")