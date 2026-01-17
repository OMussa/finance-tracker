"""
importing the Flask class to handle path/routes
"""
from flask import Flask 
from app.auth.routes import authBlueprint
from app.main.routes import main
from app.transactions.routes import transactions
from app.extensions import db , migrate
from app import models



#creating flask app instance
app = Flask(
    __name__,
    
    template_folder="../templates")
#loading config 
app.config.from_object("config.Config")
#database setup
db.init_app(app)
migrate.init_app(app,db)
    
app.register_blueprint(authBlueprint)
app.register_blueprint(main)
app.register_blueprint(transactions)


    

    
    

