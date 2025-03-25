from flask import Blueprint, render_template, jsonify
from models.delusion import Delusion

delusions_controller = Blueprint('delusions', __name__, url_prefix='/delusions')

@delusions_controller.route('/')
def index():
    titleHeader = "Delusions"
    titleSubHeader = "These are the ramblings manifested into words, my theories and ideas. Here you will find everything else."
    content = "This is the content for the Delusions page"
    return render_template('navigation/index.html', 
                           mindObjectType="Delusions",
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)

@delusions_controller.route('/data')
def get_data():
    # Get all delusions from the database
    all_delusions = Delusion.get_all()
    
    # Convert to list of dictionaries for JSON response
    cards = [delusion.to_dict() for delusion in all_delusions]
    
    # Format data for the card display
    formatted_cards = []
    for card in cards:
        formatted_cards.append({
            "id": card["id"],
            "title": card["topic"],
            "content": card["topicDesc"],
            "subtopic": card["subtopic"],
            "subtopicDesc": card["subTopicDesc"],
            "tag": card["tag"]
        })
    
    return jsonify(formatted_cards)