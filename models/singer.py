from database import db


class Singer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    photo = db.Column(db.String(100), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    albums = db.relationship('Album', backref='singer', lazy=True)
    comments = db.relationship('Comment', backref='singer', lazy=True)
    facebook_url = db.Column(db.String(100), nullable=True)
    instagram_url = db.Column(db.String(100), nullable=True)
    tiktok_url = db.Column(db.String(100), nullable=True)
    active_since = db.Column(db.Integer, nullable=True)
