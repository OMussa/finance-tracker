from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash


"""
- db -> instance of the SQLAlchemy class that allows you to use the SQLAlchemy tools conveniently without having to import each tool 
for ex. from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP  
-- fundamental data types  and classes from SQLAlchemy --
- db.Column -> a column in the datatable
- db.Integer or db.Float or db.String -> specifies type of data allowed in the columns
- db.ForeignKey -> this column is refrencing a column in a different table 
-- Constraints --
- primary_key -> main refrence point or head for each record/row 
- nullable -> should this column or row be empty? nullable by default
- 
"""
class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable = False , unique = True)
    password_hash = db.Column(db.String(255),nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow, nullable = False)
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
class transactions(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable = False)
    amount_cents = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String(50), nullable = False)
    category = db.Column(db.String(50),nullable = True)
    note = db.Column(db.String(100), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow, nullable = False)


