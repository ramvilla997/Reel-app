from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
from app.extensions import db

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
   
    app.config.from_object(config_class)

    db.init_app(app)

    from app.models import User,Video,Like,Share,Comment
    
    with app.app_context():
        db.create_all()
    

    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)
        
    return app
