from flask import Blueprint, render_template

interests_controller = Blueprint('interests', __name__, url_prefix='/interests')

@interests_controller.route('/')
def index():
    titleHeader = "Interest"
    titleSubHeader = "My interests have been described as seasonal so follow me as i grow, learn, explore, experiment and discover."
    content = "This is the content for the Interest page"
    return render_template('navigation/interests.html', 
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)