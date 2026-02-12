

from functools import wraps
from flask import session, redirect, url_for, flash, g
from app.models import users


def login_required(f): #decorator function that will be called to protect a route (@login_required)
    """
    f is the original function were decorating/protecting ex. dashboard():
    returns a wrapper function that will either redirect to login page or call the original function 
    """
    @wraps(f)  
    
    #Keep the wrapper's name/docstring the same as the original route function.
    #Flask uses the function name as the route's internal name by default.
    #Without @wraps, every decorated route would look like it's named "decorated_function"
    #so Flask would see conflicts when registering multiple routes (and url_for/debugging get messy).
    
    
    def decorated_function(*args, **kwargs): # 
        """
       wrapper function that actually does the work of the decorator. 
       parameters(*args, **kwargs) allows for this decorator to be called on route functions with arguments or keyword arguments
        """
        if 'user_id' not in session:
            # User is NOT logged in
            flash("Please log in to access this page", "error")
            return redirect(url_for('auth.login'))  
        
        return f(*args, **kwargs) # successfully logged in so we can call the original function ex. dashboard() continues to run after the decorator is applied
    return decorated_function 


def get_current_user():
    """
    Retrieves the currently logged-in user from the database.
    1. Check if 'user_id' exists in the session
    2. If it does, query the database for that user
    3. Return the user object (or None if not found)
    """
    if 'user_id' not in session:
        return None  # No one is logged in
    
    # users.query.get() is a SQLAlchemy method that finds a record by primary key (id)
    return users.query.get(session['user_id'])


def load_user_into_g():
    """
    Loads the current user into Flask's 'g' object so it's available in templates.
    
    WHY?
    -------------
    Without this, you'd have to call get_current_user() in EVERY route
    and pass user data to every template manually. 
    
    With this, you can access the current user in ANY template like:
    - {{ g.user.email }} in your HTML
    - Check if logged in: {% if g.user %}
    
    """
    # Call get_current_user() and store the result in g.user
    # Now g.user is available everywhere for this request
    g.user = get_current_user()
