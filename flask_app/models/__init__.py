from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User


class Database:
    def __init__(self):
        self.users = User.query.all()

    def get_users(self):
        return self.users

    def refresh(self):
        self.users = User.query.all()
