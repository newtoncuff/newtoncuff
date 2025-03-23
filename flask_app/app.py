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

@app.route('/thoughts')
def navigation_thoughts():
    titleHeader = "Thoughts"
    titleSubHeader = "Try and keep up with the random thoughts that invade my head and lead to the randomness that ensues."
    content = "This is the content for the Thoughts page"
    return render_template('navigation/thoughts.html', titleHeader=titleHeader, titleSubHeader=titleSubHeader, content=content)

@app.route('/passions')
def navigation_passions():
    titleHeader = "Passions"
    titleSubHeader = "I treasures these more than words can describe. They are my joy, frustration and provide motivation."
    content = "This is the content for the Passions page"
    return render_template('navigation/passions.html', titleHeader=titleHeader, titleSubHeader=titleSubHeader, content=content)

@app.route('/delusions')
def navigation_delusions():
    titleHeader = "Delusions"
    titleSubHeader = "These are my ramblings manifested into words, my theories and ideas. Here you will find everything else."
    content = "This is the content for the Delusions page"
    return render_template('navigation/delusions.html', titleHeader=titleHeader, titleSubHeader=titleSubHeader, content=content)

@app.route('/interest')
def navigation_interests():
    titleHeader = "Interest"
    titleSubHeader = "My interests have been described as seasonal so follow me as i grow, learn, explore, experiment and discover."
    content = "This is the content for the Interest page"
    return render_template('navigation/interest.html', titleHeader=titleHeader, titleSubHeader=titleSubHeader, content=content)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

