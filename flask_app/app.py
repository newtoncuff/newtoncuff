from database import database_schema
from database import database_config
from flask import Flask, render_template
from models import db
from models import User
from controllers import register_controllers

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = ( database_config.database_connection_uri )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
# Register blueprints
    register_controllers(app)
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

