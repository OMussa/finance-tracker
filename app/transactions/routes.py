from flask import Blueprint, render_template
from app.auth.decorators import login_required

transactions = Blueprint("transaction",__name__)

@transactions.route("/expense")
@login_required
def expense():
    return render_template("transactions/expense.html")

@transactions.route("/income")
@login_required
def income():
    return render_template("transactions/income.html")