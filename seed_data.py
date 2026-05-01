"""
Database seeding script for Flask Market
Refactored to support UUID-based unique barcodes and automatic seeding.
"""

import uuid
from market import app, db
from market.models import Item, User

# Sample products to add to the marketplace
SAMPLE_PRODUCTS = [
    # Smartphones
    {
        "name": "iPhone 15 Pro",
        "price": 999,
        "description": "Latest Apple iPhone with A17 Pro chip, titanium design, and advanced camera system. Features 48MP main camera and USB-C connectivity."
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "price": 1199,
        "description": "Premium Android flagship with S Pen, 200MP camera, Snapdragon 8 Gen 3, titanium frame, and 5000mAh battery with 45W charging."
    },
    {
        "name": "Google Pixel 8 Pro",
        "price": 899,
        "description": "Google's AI-powered smartphone with Tensor G3 chip, 50MP camera, 7 years of updates, and best-in-class computational photography."
    },
    {
        "name": "iPhone 16 Pro",
        "price": 1199,
        "description": "Latest Apple iPhone with A17 Pro chip, titanium design, and advanced camera system. Features 48MP main camera and USB-C connectivity."
    },
    {
        "name": "Samsung Galaxy S25 Ultra",
        "price": 1299,
        "description": "Premium Android flagship with S Pen, 200MP camera, Snapdragon 8 Gen 3, titanium frame, and 5000mAh battery with 45W charging."
    },
    # Laptops & Tablets
    {
        "name": "MacBook Air M3",
        "price": 1299,
        "description": "Ultra-thin laptop with Apple M3 chip, 15.3-inch Liquid Retina display, 18-hour battery life, and MagSafe charging."
    },
    {
        "name": "MacBook Pro 14",
        "price": 1999,
        "description": "Professional laptop with M3 Pro chip, 14-inch Liquid Retina XDR display, 17-hour battery, and studio-quality mics."
    },
    {
        "name": "Dell XPS 15",
        "price": 1599,
        "description": "Premium Windows laptop with 13th Gen Intel Core i7, NVIDIA RTX 4060, 15.6-inch OLED display, and InfinityEdge design."
    },
    {
        "name": "iPad Pro 12.9",
        "price": 1099,
        "description": "Professional tablet with M2 chip, Liquid Retina XDR display, Apple Pencil support, and all-day battery life."
    },
    {
        "name": "iPad Air",
        "price": 599,
        "description": "Powerful tablet with M1 chip, 10.9-inch Liquid Retina display, Touch ID, and support for Apple Pencil and Magic Keyboard."
    },
    # Audio
    {
        "name": "Sony WH-1000XM5",
        "price": 350,
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery, superior sound quality, and ultra-comfortable design."
    },
    {
        "name": "AirPods Pro 2",
        "price": 249,
        "description": "Wireless earbuds with active noise cancellation, adaptive audio, MagSafe charging case, and 6 hours playback."
    },
    {
        "name": "AirPods Max",
        "price": 549,
        "description": "Premium over-ear headphones with computational audio, spatial audio, aluminum cups, and 20-hour battery life."
    },
    {
        "name": "Bose SoundLink Flex",
        "price": 149,
        "description": "Portable Bluetooth speaker with deep bass, waterproof IP67 rating, 12-hour battery, and rugged silicone design."
    },
    {
        "name": "Sonos Era 300",
        "price": 449,
        "description": "Spatial audio speaker with Dolby Atmos support, six drivers, WiFi and Bluetooth, and voice control compatibility."
    },
    {
        "name": "JBL Charge 5",
        "price": 179,
        "description": "Portable Bluetooth speaker with 20-hour playtime, IP67 waterproof, powerbank function, and PartyBoost pairing."
    },
    # Wearables
    {
        "name": "Samsung Galaxy Watch 6",
        "price": 299,
        "description": "Advanced smartwatch with health monitoring, sleep tracking, sapphire crystal display, and up to 40 hours battery."
    },
    {
        "name": "Apple Watch Ultra 2",
        "price": 799,
        "description": "Rugged titanium smartwatch with 36-hour battery, precision GPS, 100m water resistance, and Action button."
    },
    {
        "name": "Apple Watch Series 9",
        "price": 399,
        "description": "Advanced smartwatch with S9 chip, double tap gesture, always-on Retina display, and crash detection."
    },
    {
        "name": "Garmin Fenix 7X",
        "price": 899,
        "description": "Premium multisport GPS watch with solar charging, 28-day battery, topo maps, and advanced training metrics."
    },
    # Gaming
    {
        "name": "Nintendo Switch OLED",
        "price": 349,
        "description": "Hybrid gaming console with vibrant 7-inch OLED screen, enhanced audio, and dock with wired LAN port."
    },
    {
        "name": "PlayStation 5",
        "price": 499,
        "description": "Next-gen gaming console with ultra-fast SSD, ray tracing, 4K gaming, haptic feedback DualSense controller."
    },
    {
        "name": "Xbox Series X",
        "price": 499,
        "description": "Powerful gaming console with 12 teraflops GPU, 1TB SSD, 4K gaming at 120fps, and Game Pass compatibility."
    },
    {
        "name": "Steam Deck OLED",
        "price": 549,
        "description": "Handheld gaming PC with 7.4-inch OLED display, AMD APU, 512GB SSD, and full Steam library access."
    },
    {
        "name": "Razer BlackWidow V4",
        "price": 229,
        "description": "Mechanical gaming keyboard with green switches, RGB Chroma lighting, magnetic wrist rest, and macro keys."
    },
    {
        "name": "Logitech G Pro X Superlight",
        "price": 159,
        "description": "Ultra-lightweight wireless gaming mouse at 63g, HERO 25K sensor, 70-hour battery, and zero-additive PTFE feet."
    },
    # Cameras & Drones
    {
        "name": "GoPro HERO12 Black",
        "price": 399,
        "description": "Action camera with 5.3K video, HyperSmooth 6.0 stabilization, waterproof to 33ft, and Emmy-winning image quality."
    },
    {
        "name": "DJI Mini 3 Pro",
        "price": 759,
        "description": "Lightweight drone under 249g with 4K/60fps video, 48MP photos, obstacle sensing, and 34-min flight time."
    },
    {
        "name": "Sony A7 IV",
        "price": 2499,
        "description": "Full-frame mirrorless camera with 33MP sensor, 4K 60p video, real-time eye AF, and 10fps continuous shooting."
    },
    {
        "name": "Canon EOS R6 Mark II",
        "price": 2299,
        "description": "Professional mirrorless with 24.2MP sensor, 40fps shooting, 6K video, and subject detection AF system."
    },
    # Smart Home
    {
        "name": "Dyson V15 Detect",
        "price": 749,
        "description": "Powerful cordless vacuum with laser dust detection, LCD screen showing particle analysis, and 60-min runtime."
    },
    {
        "name": "Apple HomePod 2nd Gen",
        "price": 299,
        "description": "Smart speaker with spatial audio, room sensing, Siri, temperature/humidity sensor, and smart home hub."
    },
    {
        "name": "Google Nest Hub Max",
        "price": 229,
        "description": "10-inch smart display with camera, Google Assistant, video calling, Nest Cam integration, and gesture control."
    },
    {
        "name": "Ring Video Doorbell Pro 2",
        "price": 249,
        "description": "Smart doorbell with 3D motion detection, 1536p HD video, head-to-toe view, and Bird's Eye View map."
    },
    {
        "name": "Philips Hue Starter Kit",
        "price": 199,
        "description": "Smart lighting kit with 4 color bulbs, Hue Bridge, 16 million colors, and voice assistant compatibility."
    }
]


def seed_database(interactive=True):
    """Add sample products to the database with unique UUID barcodes"""
    with app.app_context():
        db.create_all()
        
        # Add products
        added_count = 0
        for product in SAMPLE_PRODUCTS:
            # Generate a truly unique barcode using UUID
            # This ensures even if the name is the same, the product is a new unique stock item
            unique_barcode = str(uuid.uuid4().hex)[:16]
            
            item = Item(
                name=product["name"],
                price=product["price"],
                barcode=unique_barcode,
                description=product["description"]
            )
            db.session.add(item)
            added_count += 1
        
        db.session.commit()
        print(f"Successfully added {added_count} unique products to the database!")
        return added_count


def check_and_refill_stock():
    """Automatically refills stock if unowned items are low (< 10)"""
    with app.app_context():
        unowned_count = Item.query.filter_by(owner=None).count()
        if unowned_count < 10:
            print(f"Low stock detected ({unowned_count} items). Refilling...")
            seed_database(interactive=False)
            return True
        return False


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--clear":
        with app.app_context():
            Item.query.delete()
            db.session.commit()
            print("Database cleared.")
    else:
        seed_database()
