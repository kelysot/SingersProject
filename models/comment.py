from datetime import datetime

from database import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(20), nullable=False)

    # Foreign keys to associate comments with a user and singer
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    singer_id = db.Column(db.Integer, db.ForeignKey('singer.id'), nullable=False)
