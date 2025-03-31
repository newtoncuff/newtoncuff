# Prevent Python from writing .pyc files (compiled bytecode files) to the disk
import sys
sys.dont_write_bytecode = True

from flask import Flask
from database import database_config
from models import db
from controllers import register_controllers

def create_app():
    #Create a Flask application instance.
    app = Flask(__name__)

    # Configure the database URI for SQLAlchemy
    # This sets the connection string for the database, which is defined in `database_config.database_connection_uri`
    app.config["SQLALCHEMY_DATABASE_URI"] = ( database_config.database_connection_uri )
    
    # Disable SQLAlchemy's event system for tracking modifications to objects
    # This is set to False to save resources as it is not needed in most cases
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register blueprints aka controllere for navigation
    # This allows us to organize our routes and views into separate modules
    # and makes the application more modular and maintainable
    register_controllers(app)
    

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

