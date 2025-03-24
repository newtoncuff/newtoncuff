from flask import Blueprint, render_template

passions_controller = Blueprint('passions', __name__, url_prefix='/passions')

@passions_controller.route('/')
def index():
    titleHeader = "Passions"
    titleSubHeader = "I treasures these more than words can describe. They are my joy, frustration and provide motivation."
    content = "This is the content for the Passions page"
    return render_template('navigation/passions.html', 
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)