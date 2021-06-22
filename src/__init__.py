from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=True):
    app = Flask(__name__)

    app.config['ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_blog.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['SECRET_KEY'] = 'BCTsMiRWe5XVg44kosryuQ'

    return app

app = create_app()
db = SQLAlchemy(app)

from src import routes
from src.auth import auth, admin
from src.errors import errors

# blueprints
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(errors)