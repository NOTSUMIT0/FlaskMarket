"""
Database seeding script for Flask Market
Run this script to add sample products to the database
Usage: python seed_data.py
"""

from market import app, db
from market.models import Item, User

# Sample products to add to the marketplace
SAMPLE_PRODUCTS = [
    {
        "name": "iPhone 15 Pro",
        "price": 999,
        "barcode": "823456789012",
        "description": "Latest Apple iPhone with A17 Pro chip, titanium design, and advanced camera system. Features 48MP main camera and USB-C connectivity."
    },
    {
        "name": "MacBook Air M3",
        "price": 1299,
        "barcode": "823456789013",
        "description": "Ultra-thin laptop with Apple M3 chip, 15.3-inch Liquid Retina display, 18-hour battery life, and MagSafe charging."
    },
    {
        "name": "Sony WH-1000XM5",
        "price": 350,
        "barcode": "823456789014",
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery, superior sound quality, and ultra-comfortable design."
    },
    {
        "name": "Samsung Galaxy Watch 6",
        "price": 299,
        "barcode": "823456789015",
        "description": "Advanced smartwatch with health monitoring, sleep tracking, sapphire crystal display, and up to 40 hours battery."
    },
    {
        "name": "iPad Pro 12.9",
        "price": 1099,
        "barcode": "823456789016",
        "description": "Professional tablet with M2 chip, Liquid Retina XDR display, Apple Pencil support, and all-day battery life."
    },
    {
        "name": "Nintendo Switch OLED",
        "price": 349,
        "barcode": "823456789017",
        "description": "Hybrid gaming console with vibrant 7-inch OLED screen, enhanced audio, and dock with wired LAN port."
    },
    {
        "name": "DJI Mini 3 Pro",
        "price": 759,
        "barcode": "823456789018",
        "description": "Lightweight drone under 249g with 4K/60fps video, 48MP photos, obstacle sensing, and 34-min flight time."
    },
    {
        "name": "Dyson V15 Detect",
        "price": 749,
        "barcode": "823456789019",
        "description": "Powerful cordless vacuum with laser dust detection, LCD screen showing particle analysis, and 60-min runtime."
    },
    {
        "name": "AirPods Pro 2",
        "price": 249,
        "barcode": "823456789020",
        "description": "Wireless earbuds with active noise cancellation, adaptive audio, MagSafe charging case, and 6 hours playback."
    },
    {
        "name": "Bose SoundLink Flex",
        "price": 149,
        "barcode": "823456789021",
        "description": "Portable Bluetooth speaker with deep bass, waterproof IP67 rating, 12-hour battery, and rugged silicone design."
    },
    {
        "name": "Kindle Paperwhite",
        "price": 139,
        "barcode": "823456789022",
        "description": "E-reader with 6.8-inch display, adjustable warm light, waterproof design, and weeks of battery life."
    },
    {
        "name": "GoPro HERO12 Black",
        "price": 399,
        "barcode": "823456789023",
        "description": "Action camera with 5.3K video, HyperSmooth 6.0 stabilization, waterproof to 33ft, and Emmy-winning image quality."
    }
    ,    {
        "name": "FlashLight",
        "price": 399,
        "barcode": "823456789000",
        "description": "A flashlight with 5.3K video, HyperSmooth 6.0 stabilization, waterproof to 33ft, and Emmy-winning image quality."
    }
]


def seed_database():
    """Add sample products to the database"""
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Check if products already exist
        existing_items = Item.query.count()
        if existing_items > 0:
            print(f"Database already has {existing_items} items.")
            response = input("Do you want to add more items anyway? (y/n): ")
            if response.lower() != 'y':
                print("Seeding cancelled.")
                return
        
        # Add products
        added_count = 0
        for product in SAMPLE_PRODUCTS:
            # Check if product already exists
            existing = Item.query.filter_by(barcode=product["barcode"]).first()
            if existing:
                print(f"Skipping {product['name']} - already exists")
                continue
            
            item = Item(
                name=product["name"],
                price=product["price"],
                barcode=product["barcode"],
                description=product["description"]
            )
            db.session.add(item)
            added_count += 1
            print(f"Added: {product['name']} - ${product['price']}")
        
        db.session.commit()
        print(f"\n✅ Successfully added {added_count} products to the database!")
        print(f"Total items in database: {Item.query.count()}")


def clear_database():
    """Clear all items from the database"""
    with app.app_context():
        response = input("⚠️  Are you sure you want to delete ALL items? (yes/no): ")
        if response.lower() == 'yes':
            Item.query.delete()
            db.session.commit()
            print("✅ All items have been deleted.")
        else:
            print("Cancelled.")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--clear":
        clear_database()
    else:
        seed_database()
