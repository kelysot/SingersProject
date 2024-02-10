from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from database import db
from routes.user import user_bp
from routes.singer import singer_bp
from routes.comment import comment_bp
from routes.user import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '6Y1FjuHvbnqZr3rPa2lsCMrvJNQOpUsvFLMJ5ocrvsg='
app.config['JWT_SECRET_KEY'] = 'F2TT0QbOx1+D5LsJAJpdO5EDHd0+/nNsbTIgj+DJFz8='
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///singers_app.db"
db.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(singer_bp)
app.register_blueprint(comment_bp)


if __name__ == "__main__":
    app.run(debug=True)
