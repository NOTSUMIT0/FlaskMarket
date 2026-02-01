"""
Database seeding script for Flask Market
Run this script to add sample products to the database
Usage: python seed_data.py
"""

from market import app, db
from market.models import Item, User

# Sample products to add to the marketplace
SAMPLE_PRODUCTS = [
    # Smartphones
    {
        "name": "iPhone 15 Pro",
        "price": 999,
        "barcode": "823456789012",
        "description": "Latest Apple iPhone with A17 Pro chip, titanium design, and advanced camera system. Features 48MP main camera and USB-C connectivity."
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "price": 1199,
        "barcode": "823456789030",
        "description": "Premium Android flagship with S Pen, 200MP camera, Snapdragon 8 Gen 3, titanium frame, and 5000mAh battery with 45W charging."
    },
    {
        "name": "Google Pixel 8 Pro",
        "price": 899,
        "barcode": "823456789031",
        "description": "Google's AI-powered smartphone with Tensor G3 chip, 50MP camera, 7 years of updates, and best-in-class computational photography."
    },
    
    # Laptops & Tablets
    {
        "name": "MacBook Air M3",
        "price": 1299,
        "barcode": "823456789013",
        "description": "Ultra-thin laptop with Apple M3 chip, 15.3-inch Liquid Retina display, 18-hour battery life, and MagSafe charging."
    },
    {
        "name": "MacBook Pro 14",
        "price": 1999,
        "barcode": "823456789032",
        "description": "Professional laptop with M3 Pro chip, 14-inch Liquid Retina XDR display, 17-hour battery, and studio-quality mics."
    },
    {
        "name": "Dell XPS 15",
        "price": 1599,
        "barcode": "823456789033",
        "description": "Premium Windows laptop with 13th Gen Intel Core i7, NVIDIA RTX 4060, 15.6-inch OLED display, and InfinityEdge design."
    },
    {
        "name": "iPad Pro 12.9",
        "price": 1099,
        "barcode": "823456789016",
        "description": "Professional tablet with M2 chip, Liquid Retina XDR display, Apple Pencil support, and all-day battery life."
    },
    {
        "name": "iPad Air",
        "price": 599,
        "barcode": "823456789034",
        "description": "Powerful tablet with M1 chip, 10.9-inch Liquid Retina display, Touch ID, and support for Apple Pencil and Magic Keyboard."
    },
    
    # Audio
    {
        "name": "Sony WH-1000XM5",
        "price": 350,
        "barcode": "823456789014",
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery, superior sound quality, and ultra-comfortable design."
    },
    {
        "name": "AirPods Pro 2",
        "price": 249,
        "barcode": "823456789020",
        "description": "Wireless earbuds with active noise cancellation, adaptive audio, MagSafe charging case, and 6 hours playback."
    },
    {
        "name": "AirPods Max",
        "price": 549,
        "barcode": "823456789035",
        "description": "Premium over-ear headphones with computational audio, spatial audio, aluminum cups, and 20-hour battery life."
    },
    {
        "name": "Bose SoundLink Flex",
        "price": 149,
        "barcode": "823456789021",
        "description": "Portable Bluetooth speaker with deep bass, waterproof IP67 rating, 12-hour battery, and rugged silicone design."
    },
    {
        "name": "Sonos Era 300",
        "price": 449,
        "barcode": "823456789036",
        "description": "Spatial audio speaker with Dolby Atmos support, six drivers, WiFi and Bluetooth, and voice control compatibility."
    },
    {
        "name": "JBL Charge 5",
        "price": 179,
        "barcode": "823456789037",
        "description": "Portable Bluetooth speaker with 20-hour playtime, IP67 waterproof, powerbank function, and PartyBoost pairing."
    },
    
    # Wearables
    {
        "name": "Samsung Galaxy Watch 6",
        "price": 299,
        "barcode": "823456789015",
        "description": "Advanced smartwatch with health monitoring, sleep tracking, sapphire crystal display, and up to 40 hours battery."
    },
    {
        "name": "Apple Watch Ultra 2",
        "price": 799,
        "barcode": "823456789038",
        "description": "Rugged titanium smartwatch with 36-hour battery, precision GPS, 100m water resistance, and Action button."
    },
    {
        "name": "Apple Watch Series 9",
        "price": 399,
        "barcode": "823456789039",
        "description": "Advanced smartwatch with S9 chip, double tap gesture, always-on Retina display, and crash detection."
    },
    {
        "name": "Garmin Fenix 7X",
        "price": 899,
        "barcode": "823456789040",
        "description": "Premium multisport GPS watch with solar charging, 28-day battery, topo maps, and advanced training metrics."
    },
    
    # Gaming
    {
        "name": "Nintendo Switch OLED",
        "price": 349,
        "barcode": "823456789017",
        "description": "Hybrid gaming console with vibrant 7-inch OLED screen, enhanced audio, and dock with wired LAN port."
    },
    {
        "name": "PlayStation 5",
        "price": 499,
        "barcode": "823456789041",
        "description": "Next-gen gaming console with ultra-fast SSD, ray tracing, 4K gaming, haptic feedback DualSense controller."
    },
    {
        "name": "Xbox Series X",
        "price": 499,
        "barcode": "823456789042",
        "description": "Powerful gaming console with 12 teraflops GPU, 1TB SSD, 4K gaming at 120fps, and Game Pass compatibility."
    },
    {
        "name": "Steam Deck OLED",
        "price": 549,
        "barcode": "823456789043",
        "description": "Handheld gaming PC with 7.4-inch OLED display, AMD APU, 512GB SSD, and full Steam library access."
    },
    {
        "name": "Razer BlackWidow V4",
        "price": 229,
        "barcode": "823456789044",
        "description": "Mechanical gaming keyboard with green switches, RGB Chroma lighting, magnetic wrist rest, and macro keys."
    },
    {
        "name": "Logitech G Pro X Superlight",
        "price": 159,
        "barcode": "823456789045",
        "description": "Ultra-lightweight wireless gaming mouse at 63g, HERO 25K sensor, 70-hour battery, and zero-additive PTFE feet."
    },
    
    # Cameras & Drones
    {
        "name": "GoPro HERO12 Black",
        "price": 399,
        "barcode": "823456789023",
        "description": "Action camera with 5.3K video, HyperSmooth 6.0 stabilization, waterproof to 33ft, and Emmy-winning image quality."
    },
    {
        "name": "DJI Mini 3 Pro",
        "price": 759,
        "barcode": "823456789018",
        "description": "Lightweight drone under 249g with 4K/60fps video, 48MP photos, obstacle sensing, and 34-min flight time."
    },
    {
        "name": "Sony A7 IV",
        "price": 2499,
        "barcode": "823456789046",
        "description": "Full-frame mirrorless camera with 33MP sensor, 4K 60p video, real-time eye AF, and 10fps continuous shooting."
    },
    {
        "name": "Canon EOS R6 Mark II",
        "price": 2299,
        "barcode": "823456789047",
        "description": "Professional mirrorless with 24.2MP sensor, 40fps shooting, 6K video, and subject detection AF system."
    },
    
    # Smart Home
    {
        "name": "Dyson V15 Detect",
        "price": 749,
        "barcode": "823456789019",
        "description": "Powerful cordless vacuum with laser dust detection, LCD screen showing particle analysis, and 60-min runtime."
    },
    {
        "name": "Apple HomePod 2nd Gen",
        "price": 299,
        "barcode": "823456789048",
        "description": "Smart speaker with spatial audio, room sensing, Siri, temperature/humidity sensor, and smart home hub."
    },
    {
        "name": "Google Nest Hub Max",
        "price": 229,
        "barcode": "823456789049",
        "description": "10-inch smart display with camera, Google Assistant, video calling, Nest Cam integration, and gesture control."
    },
    {
        "name": "Ring Video Doorbell Pro 2",
        "price": 249,
        "barcode": "823456789050",
        "description": "Smart doorbell with 3D motion detection, 1536p HD video, head-to-toe view, and Bird's Eye View map."
    },
    {
        "name": "Philips Hue Starter Kit",
        "price": 199,
        "barcode": "823456789051",
        "description": "Smart lighting kit with 4 color bulbs, Hue Bridge, 16 million colors, and voice assistant compatibility."
    },
    
    # E-Readers & Accessories
    {
        "name": "Kindle Paperwhite",
        "price": 139,
        "barcode": "823456789022",
        "description": "E-reader with 6.8-inch display, adjustable warm light, waterproof design, and weeks of battery life."
    },
    {
        "name": "Kindle Scribe",
        "price": 339,
        "barcode": "823456789052",
        "description": "E-reader and digital notebook with 10.2-inch display, included Premium Pen, and handwriting-to-text conversion."
    },
    {
        "name": "Anker 737 Power Bank",
        "price": 149,
        "barcode": "823456789053",
        "description": "140W portable charger with 24,000mAh capacity, smart display, USB-C/USB-A ports, and laptop charging support."
    },
    {
        "name": "Samsung T7 Shield SSD",
        "price": 159,
        "barcode": "823456789054",
        "description": "Portable 2TB SSD with IP65 water/dust resistance, 1,050MB/s transfer speed, and shock-resistant design."
    },
    {
        "name": "Apple Magic Keyboard",
        "price": 299,
        "barcode": "823456789055",
        "description": "Wireless keyboard for iPad Pro with trackpad, backlit keys, USB-C charging, and floating cantilever design."
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
