from .mindObjects import MindObject
from . import db

class Delusion(MindObject):
    """
    Represents a delusion - inherited from MindObject base class
    """
    __tablename__ = "Delusions"
    
    # Delusion-specific columns (if any)
    # severity = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f"<Delusion {self.topic}: {self.subtopic}>"