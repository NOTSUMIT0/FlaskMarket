# 🛒 Flask Market

A modern, premium e-commerce marketplace built with Flask. Features a stunning dark theme UI, user authentication, shopping cart, and PostgreSQL database support.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue?logo=postgresql)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?logo=tailwind-css)

##  Features

###  User Authentication
- **Register** - Create account with username, email, and password
- **Login/Logout** - Secure session-based authentication
- **Password Hashing** - Bcrypt encryption for security
- **Starting Budget** - New users get $10,000 to start shopping

###  Shopping Experience
- **Product Catalog** - Browse available products with images, prices, and descriptions
- **Product Details Modal** - View product description, barcode, and ID
- **Buy Now** - Instant purchase with confirmation modal
- **Shopping Cart** - Add multiple items to cart and purchase together
- **Sell Items** - Sell your owned items back to the marketplace

###  Inventory Management
- **My Items Sidebar** - View all items you own
- **Sell Functionality** - Put items back on market for others to buy
- **Real-time Updates** - Balance and inventory update instantly

###  Modern UI/UX
- **Dark Theme** - Premium glassmorphism design
- **Responsive Layout** - Works on desktop and mobile
- **Smooth Animations** - Hover effects, modals, and transitions
- **Tailwind CSS** - Utility-first styling

##  Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/FlaskMarket.git
cd FlaskMarket
```

2. **Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///market.db  # or PostgreSQL URL
```

5. **Initialize database with products**
```bash
python seed_data.py
```

6. **Run the application**
```bash
python run.py
```

7. **Open browser**
```
http://localhost:5000
```

##  Project Structure

```
FlaskMarket/
├── market/
│   ├── __init__.py          # App initialization
│   ├── routes.py             # URL routes and views
│   ├── models.py             # Database models (User, Item)
│   ├── forms.py              # WTForms for login/register
│   ├── config.py             # App configuration
│   ├── templates/            # Jinja2 HTML templates
│   │   ├── base.html         # Base template
│   │   ├── home.html         # Landing page
│   │   ├── market.html       # Main marketplace
│   │   ├── login.html        # Login page
│   │   └── register.html     # Registration page
│   └── static/               # CSS, JS, images
├── run.py                    # Application entry point
├── seed_data.py              # Database seeding script
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables
```

##  Database Models

### User
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| username | String(30) | Unique username |
| email_address | String(50) | Unique email |
| password_hash | String(60) | Bcrypt hash |
| budget | Integer | User's balance (default: $10,000) |

### Item
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| name | String(30) | Product name |
| price | Integer | Price in dollars |
| barcode | String(12) | Unique barcode |
| description | String(1024) | Product description |
| owner | Integer | FK to User (null if available) |

##  Technologies

- **Backend**: Flask 3.0, SQLAlchemy, Flask-Login, Flask-Bcrypt
- **Frontend**: Tailwind CSS, Font Awesome, Vanilla JavaScript
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Deployment**: Render, Gunicorn

##  Dependencies

```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-WTF==1.2.1
WTForms==3.1.1
email-validator==2.1.0
python-dotenv==1.0.0
psycopg2-binary==2.9.9
gunicorn==21.2.0
```


##  Screenshots

### Home Page
- Hero section with animated orbs
- Stats section (Products, Users, Transactions)
- Features section
- Call-to-action

### Market Page
- Left sidebar: Shopping Cart
- Center: Product grid with cards
- Right sidebar: My Items (sell)
- Modals for details, buy, and sell confirmations

##  Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request


⭐ Star this repo if you find it helpful!
