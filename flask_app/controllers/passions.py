from flask import Blueprint, render_template, jsonify
from models.passion import Passion

passions_controller = Blueprint('passions', __name__, url_prefix='/passions')

@passions_controller.route('/')
def index():
    titleHeader = "Passions"
    titleSubHeader = "I treasures these more than words can describe. They are my joy, frustration and provide motivation."
    content = "This is the content for the Passions page"
    return render_template('navigation/index.html', 
                           mindObjectType="Passions",
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)

@passions_controller.route('/data')
def get_data():
    # Get all passions from the database
    all_passions = Passion.get_all()
    
    # Convert to list of dictionaries for JSON response
    cards = [passion.to_dict() for passion in all_passions]
    
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