import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.config import config

app = Flask(__name__)

# Load configuration based on environment
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Ensure the instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from . import routes

# Create database tables within application context
# Wrapped in try-except to prevent startup failure if DB is temporarily unavailable
try:
    with app.app_context():
        db.create_all()
        print("Database tables verified/created.")
except Exception as e:
    print(f"Warning: Could not initialize database tables: {e}")
