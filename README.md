# Universal Cart

A premium, high-end e-commerce marketplace built with the Flask web framework. This application features a professional dark-themed user interface, cinematic authentication flows, dynamic category-based browsing, and an integrated flash-deals engine with PostgreSQL backend support.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue?logo=postgresql)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?logo=tailwind-css)

## Project Overview

Universal Cart is designed to provide a high-performance shopping experience. It transitions away from traditional ecommerce layouts toward a modern, tech-focused aesthetic. The platform handles real-time inventory management, secure user sessions, and dynamic pricing updates across multiple specialized pages.

## Key Features

### Advanced User Authentication
- **Cinematic Auth Flow**: The Login and Register pages utilize a split-screen architectural pattern. The left side handles form data validation, while the right side features a high-definition looping MP4 background with glassmorphic overlays.
- **Session Security**: Implemented using Flask-Login with secure cookie handling and Bcrypt password hashing for industry-standard data protection.
- **Onboarding Bonus**: Every new registration is automatically credited with a $10,000 starting balance stored securely in the PostgreSQL database.

### Product Ecosystem
- **Intelligent Categories**: Specialized views for Smartphones, Laptops, Gaming gear, and Accessories. Each category is represented by custom-designed 3D renders that use deep-shadow and glow effects to create a premium feel.
- **Flash Deals Engine**: A dedicated promotional page that dynamically calculates 20% discounts on active marketplace items. It utilizes a custom Jinja2 filter logic to display original vs. discounted prices in real-time.
- **Unified Marketplace**: A central hub where users can browse, purchase, and sell items. It includes a real-time sidebar for quick cart access and inventory tracking.

### Inventory & Transaction System
- **Atomic Purchases**: Transactions are handled with database integrity in mind, ensuring that item ownership transfers and budget updates occur simultaneously or not at all.
- **Multi-Item Cart**: Users can stage multiple products in their local session cart before committing to a bulk purchase, optimizing the transaction flow.
- **Resale Market**: A circular economy feature allowing users to sell their owned inventory back to the marketplace, instantly liquidating assets to increase their buying power.

## Technical Implementation

### Frontend Stack
- **Styling**: Built with Tailwind CSS 3.0, focusing on a custom color palette of deep blacks (#0a0a0f) and accent blues.
- **Animations**: Uses custom CSS keyframes and Tailwind utility classes to handle smooth transitions and glassmorphic hover effects.
- **Typography**: Integrated Google Fonts (Inter and Outfit) to provide a modern, readable interface.

### Backend Stack
- **Framework**: Flask 3.0 utilizing a modular blueprint-like structure.
- **Database**: SQLAlchemy ORM for seamless switching between SQLite (development) and PostgreSQL (production).
- **Forms**: WTForms for robust client-side and server-side validation of user inputs.

## Quick Start

### Prerequisites
- Python 3.9+
- Pip package manager
- PostgreSQL (optional for local dev)

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

## Project Structure
```
FlaskMarket/
├── market/
│   ├── __init__.py          # App initialization and logging config
│   ├── routes.py             # Route handlers and business logic
│   ├── models.py             # User and Item database schemas
│   ├── forms.py              # Input validation and sanitization
│   ├── templates/            # Jinja2 template ecosystem
│   │   ├── base.html         # Global navigation, footer, and modals
│   │   ├── categories.html   # 3D category grid
│   │   ├── deals.html        # Discounted product display
│   │   └── auth/             # Split-screen login and registration
│   └── static/               # CSS, JS, 3D Images, and Cinematic Videos
├── run.py                    # Entry point for the WSGI server
├── seed_data.py              # Script for populating items and users
└── requirements.txt          # Full list of Python dependencies
```

## Maintenance and Contributing
The project is built to be modular. To add a new category, simply add the relevant route in `routes.py` and create a corresponding template extending `base.html`. For product updates, modify `seed_data.py` and re-run the initialization script.

---
**Universal Cart** — High-performance tech marketplace.
