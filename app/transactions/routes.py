from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.auth.decorators import login_required
from app import models,extensions

transactions = Blueprint("transaction",__name__)

@transactions.route("/expense", methods=["GET", "POST"])
@login_required
def expense():
    if request.method == "POST":
        # Get form data
        amount = (request.form.get("amount") or "").strip() 
        category = (request.form.get("category") or "").strip() 
        note = (request.form.get("note")or "").strip()
       
        
        # Validate amount is not empty
        if  not amount:
            flash("Amount cannot be empty","error")
            return render_template("transactions/expense.html")
    
        
        # Convert amount to cents with error handling
        try:
            amount = int(float(amount) * 100) 
        except ValueError as e:
            flash("Invalid amount. Please enter a valid number (e.g., 19.99)", "error")
            return render_template("transactions/expense.html")
       
        
        # Validate amount is positive
        if amount <= 0:
            flash("Amount cannot be negative","error")
            return render_template("transactions/expense.html")


        
        #Validate category is not empty
        if not category:
            flash("Category cannot be empty","error")
            return render_template("transactions/expense.html")

        
        # Create new transaction object
        new_expense = models.transactions(user_id=session["user_id"],amount_cents=amount, type="expense", category=category, note=note)
        
        # Save to database with error handling
        try:
            record = new_expense
            extensions.db.session.add(record)
            extensions.db.session.commit()
            flash("Successfully added expense ", "success")
            return redirect(url_for("main_bp.dashboard"))
        except Exception as e:
            extensions.db.session.rollback()
            flash("error adding expense","error")
            return render_template("transactions/expense.html")

        
    return render_template("transactions/expense.html")



@transactions.route("/income", methods=["GET", "POST"])
@login_required
def income():
    if request.method == "POST":
        amount = (request.form.get("amount")or "").strip()
        category = (request.form.get("category") or "").strip()
        note = (request.form.get("note")or "").strip()

        if not amount:
            flash("Amount cannot be empty","error")
            return render_template("transactions/income.html")
        
        try:
            amount = int(float(amount) *100)
        except ValueError as e:
            flash("Invalid amount. Please enter a valid number (e.g., 19.99)", "error")
            return render_template("transactions/income.html")

        if amount <= 0:
            flash("Amount cannot be negative","error")
            return render_template("transactions/income.html")


        if not category:
            flash("Category cannot be empty","error")
            return render_template("transactions/income.html")

        new_income= models.transactions(user_id = session["user_id"], amount_cents = amount, type ="income", category = category, note = note)
        
        try:
            record = new_income
            extensions.db.session.add(record)
            extensions.db.session.commit()
            flash("successfully added", "success")
            return redirect(url_for("main_bp.dashboard"))
        except Exception as e:
            extensions.db.session.rollback()
            flash("error adding","error")
            return render_template("transactions/income.html")
        
    
    # GET request: show the form
    return render_template("transactions/income.html")