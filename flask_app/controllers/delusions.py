from flask import Blueprint, render_template

delusions_controller = Blueprint('delusions', __name__, url_prefix='/delusions')

@delusions_controller.route('/')
def index():
    titleHeader = "Delusions"
    titleSubHeader = "These are the ramblings manifested into words, my theories and ideas. Here you will find everything else."
    content = "This is the content for the Delusions page"
    return render_template('navigation/delusions.html', 
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)