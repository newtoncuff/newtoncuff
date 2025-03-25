from flask import Blueprint, render_template, jsonify
from models.interest import Interest

interests_controller = Blueprint('interests', __name__, url_prefix='/interests')

@interests_controller.route('/')
def index():
    titleHeader = "Interest"
    titleSubHeader = "My interests have been described as seasonal so follow me as i grow, learn, explore, experiment and discover."
    content = "This is the content for the Interest page"
    return render_template('navigation/index.html', 
                           mindObjectType="Interests",
                           titleHeader=titleHeader, 
                           titleSubHeader=titleSubHeader, 
                           content=content)

@interests_controller.route('/data')
def get_data():
    # Get all interests from the database
    all_interests = Interest.get_all()
    
    # Convert to list of dictionaries for JSON response
    cards = [interest.to_dict() for interest in all_interests]
    
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