import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.config import config

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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


# Create database tables within application context
# Wrapped in logic to auto-fix the database schema if it's broken or empty
try:
    with app.app_context():
        from market.models import Item
        
        # 1. Try to create all tables (if they don't exist)
        db.create_all()
        
        # 2. Check if the schema is valid and if we need to refill
        try:
            unowned_count = Item.query.filter_by(owner=None).count()
            
            # If market is empty or very low, refill it
            if unowned_count < 10:
                print(f"Auto-Refill: Low stock detected ({unowned_count}). Seeding...")
                from seed_data import seed_database
                seed_database()
                
        except Exception as schema_error:
            # If we get a column error, it means the old schema exists. 
            # We must drop and recreate to apply the new UUID and non-unique name rules.
            print(f"Database schema mismatch detected: {schema_error}. Fixing...")
            db.session.remove()
            Item.__table__.drop(db.engine)
            db.create_all()
            from seed_data import seed_database
            seed_database()
            print("Database schema fixed and market refilled!")

except Exception as e:
    print(f"Critical error during database initialization: {e}")

from . import routes
