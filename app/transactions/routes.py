from flask import Blueprint, render_template

transactions = Blueprint("transaction",__name__)

@transactions.route("/expense")
def expense():
    return render_template("transactions/expense.html")

@transactions.route("/income")
def income():
    return render_template("transactions/income.html")