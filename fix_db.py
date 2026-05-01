from market import app, db
from market.models import Item

def fix_database():
    with app.app_context():
        print("Dropping Item table to update schema...")
        # We only drop the Item table to preserve User accounts
        Item.__table__.drop(db.engine)
        print("Recreating Item table with new UUID-compatible schema...")
        db.create_all()
        print("Schema updated successfully!")
        
        # Now seed it fresh
        from seed_data import seed_database
        seed_database()

if __name__ == "__main__":
    fix_database()
