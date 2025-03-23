from database import database_schema
from database import database_config
from flask import Flask, render_template
from models import db
from models import User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ( database_config.database_connection_uri )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    title = "Home"

    try:
        # Query the User table
        users = User.query.all()
        content = ""
        for user in users:
            content += f"User: {user.username}, Email: {user.email}<br>"
    except Exception as e:
        print(f"Error querying User table: {e}")  # Debugging output
        content = f"Error: {e}"
    return render_template("home.html", title=title, content=content)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

