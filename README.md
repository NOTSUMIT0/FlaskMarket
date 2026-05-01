# 🛒 Universal Cart

A premium, high-end e-commerce marketplace built with Flask. Features a stunning dark-themed UI, user authentication with cinematic auth pages, categorized product browsing, exclusive flash deals, and PostgreSQL support.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue?logo=postgresql)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?logo=tailwind-css)

## 🌟 Key Features

### 🚀 Modern Architecture
- **Branding**: Rebranded as **Universal Cart** with a premium tech-focused aesthetic.
- **Cinematic Auth**: Redesigned Login and Register pages featuring a split-screen layout with looping cinematic video backgrounds.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop viewing.

### 📦 Shopping Experience
- **Product Catalog**: Browse a wide range of premium electronics with detailed specifications.
- **Dynamic Categories**: Dedicated pages for **Smartphones**, **Laptops**, **Gaming**, and **Accessories** with 3D imagery.
- **Exclusive Deals**: A flash-sale page showcasing real marketplace products with exclusive 20% discounts.
- **Shopping Cart**: Advanced multi-item cart system for bulk purchases.
- **Inventory Management**: Sidebar trackers for owned items and real-time budget updates.

### 🔒 Security & Data
- **Secure Authentication**: Session-based login with password hashing via Bcrypt.
- **PostgreSQL Integration**: Production-ready database support for high-performance data handling.
- **Starting Bonus**: New members receive an instant $10,000 starting balance.

## 🎨 Visual Assets
The project integrates premium 3D assets and animations:
- **3D Renders**: Custom-generated 3D models for each product category.
- **Glassmorphism**: Sleek, transparent UI elements with vibrant accent glows.
- **Video Backgrounds**: High-quality looping MP4 backgrounds for authentication flows.

## 🛠️ Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL (optional, default is SQLite)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/NOTSUMIT0/FlaskMarket.git
cd FlaskMarket
```

2. **Create virtual environment**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate  
# Linux/Mac
source .venv/bin/activate  
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory:
```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///market.db  # Use PostgreSQL URL for production
```

5. **Initialize Database**
```bash
python seed_data.py
```

6. **Run Application**
```bash
python run.py
```

## 📂 Project Structure
```
FlaskMarket/
├── market/
│   ├── routes.py             # Route handlers (Home, Market, Categories, Deals, Auth)
│   ├── models.py             # SQLAlchemy Models (User, Item)
│   ├── forms.py              # WTForms (Login, Register, Purchase, Sell)
│   ├── templates/            # HTML Templates (Jinja2)
│   │   ├── base.html         # Global Layout & Navigation
│   │   ├── categories.html   # Category Grid
│   │   ├── deals.html        # Flash Sale Page
│   │   └── auth/             # Login & Register
│   └── static/               # CSS, JS, Images, Videos
├── run.py                    # App Entry Point
└── seed_data.py              # Production Seeding Script
```

## 📸 Page Highlights

- **Home**: Dynamic hero section with premium 3D laptop renders.
- **Categories**: Interactive grid showcasing high-end tech categories.
- **Deals**: High-energy flash sale banner with real market item discounts.
- **Market**: Full-featured trading floor with cart and inventory management.

## 🤝 Contributing
Contributions are welcome! Please fork the repo and open a PR for any features or bug fixes.

---
⭐ **Universal Cart** — *Your premium tech destination.*
