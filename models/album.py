from database import db


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(100), nullable=True)
    singer_id = db.Column(db.Integer, db.ForeignKey('singer.id'), nullable=False)

