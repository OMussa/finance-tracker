<<<<<<< HEAD
# app/transactions/routes.py

"""
File Purpose:
    Handles pages related to creating new income or expense transactions.

Blueprint:
    transactions_bp - all URLs start with /transactions
"""

from flask import Blueprint, render_template

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


@transactions_bp.route("/income/new")
def new_income():
    """
    Purpose:
        Display the form to create a new income entry.

    Arguments:
        None

    Returns:
        HTML page: templates/transactions/new_income.html

    When It's Used:
        User visits /transactions/income/new
    """
    return render_template("transactions/new_income.html")


@transactions_bp.route("/expense/new")
def new_expense():
    """
    Purpose:
        Display the form to create a new expense entry.

    Arguments:
        None

    Returns:
        HTML page: templates/transactions/new_expense.html

    When It's Used:
        User visits /transactions/expense/new
    """
    return render_template("transactions/new_expense.html")
=======
from flask import Blueprint, render_template

transactions = Blueprint("transaction",__name__)

@transactions.route("/expense")
def expense():
    return render_template("transactions/expense.html")

@transactions.route("/income")
def income():
    return render_template("transactions/income.html")
>>>>>>> origin/main
