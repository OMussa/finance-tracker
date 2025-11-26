<<<<<<< HEAD
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/ping")
    def ping ():
        return "pong"
    
    return app
=======
"""
importing the Flask class to handle path/routes
"""
from flask import Flask , render_template
from app.auth.routes import authBlueprint
from app.main.routes import main
from app.transactions.routes import transactions




app = Flask(
    __name__,
    
    template_folder="../templates")
    
app.register_blueprint(authBlueprint)
app.register_blueprint(main)
app.register_blueprint(transactions)


    

    
    

>>>>>>> origin/main
