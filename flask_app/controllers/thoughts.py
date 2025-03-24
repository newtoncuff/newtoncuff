from flask import Blueprint, render_template

thoughts_controller = Blueprint('thoughts', __name__, url_prefix='/thoughts')

@thoughts_controller.route('/')
def index():
    titleHeader = "Thoughts"
    titleSubHeader = "Try and keep up with the random thoughts that invade my head and lead to the randomness that ensues."
    content = "This is the content for the Thoughts page"
    return render_template('navigation/thoughts.html', 
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)