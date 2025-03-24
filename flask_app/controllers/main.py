from flask import Blueprint, render_template
from models import User

main_controller = Blueprint('main', __name__)

@main_controller.route("/")
def home():
    title = "Home"
    return render_template("home.html", title=title)
"""     try:
        # Query the User table
        users = User.query.all()
        content = ""
        for user in users:
            content += f"User: {user.username}, Email: {user.email}<br>"
    except Exception as e:
        print(f"Error querying User table: {e}")  # Debugging output
        content = f"Error: {e}" """
     
#, content=content)