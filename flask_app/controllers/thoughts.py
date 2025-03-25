from flask import Blueprint, render_template, jsonify
from models.thought import Thought

thoughts_controller = Blueprint('thoughts', __name__, url_prefix='/thoughts')

@thoughts_controller.route('/')
def index():
    titleHeader = "Thoughts"
    titleSubHeader = "Try and keep up with the random thoughts that invade my head and lead to the randomness that ensues."
    content = "This is the content for the Thoughts page"
    return render_template('navigation/index.html', 
                           mindObjectType="Thoughts",
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)

@thoughts_controller.route('/data')
def get_data():
    # Get all thoughts from the database
    all_thoughts = Thought.get_all()
    
    # Convert to list of dictionaries for JSON response
    cards = [thought.to_dict() for thought in all_thoughts]
    
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