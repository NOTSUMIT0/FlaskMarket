# Deploying Flask Market to Render - Complete Guide

## Prerequisites ✅

Your project already has:
- `requirements.txt` with `gunicorn` and `psycopg2-binary`
- PostgreSQL database URL from Render
- Proper config.py for production

---

## Step 1: Initialize Database with Products

Before deploying, add your products to the PostgreSQL database:

```bash
# In your project folder, open Python shell
python

# Run these commands:
from market import app, db
from market.models import Item

with app.app_context():
    db.create_all()
    
    # Add products
    items = [
        Item(name='Laptop', price=1000, barcode='100000000001', description='High performance laptop'),
        Item(name='iPhone 15 Pro', price=999, barcode='100000000002', description='Latest Apple iPhone with A17 Pro chip'),
        Item(name='MacBook Air M3', price=1299, barcode='100000000003', description='Ultra-thin laptop with Apple M3 chip'),
        Item(name='Sony WH-1000XM5', price=350, barcode='100000000004', description='Industry-leading noise cancellation'),
        Item(name='Samsung Galaxy Watch', price=299, barcode='100000000005', description='Advanced smartwatch'),
        Item(name='iPad Pro 12.9', price=1099, barcode='100000000006', description='Professional tablet with M2 chip'),
        Item(name='Nintendo Switch OLED', price=349, barcode='100000000007', description='Hybrid gaming console'),
    ]
    
    for item in items:
        existing = Item.query.filter_by(name=item.name).first()
        if not existing:
            db.session.add(item)
    
    db.session.commit()
    print("Products added!")
```

---

## Step 2: Push to GitHub

```bash
# Initialize git (if not done)
git init

# Add files
git add .

# Commit
git commit -m "Initial commit - Flask Market ready for deployment"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/FlaskMarket.git
git branch -M main
git push -u origin main
```

---

## Step 3: Create Web Service on Render

1. Go to [render.com](https://render.com) → Dashboard
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account if not connected
4. Select your **FlaskMarket** repository
5. Configure:

| Setting | Value |
|---------|-------|
| **Name** | `flask-market` (or your choice) |
| **Region** | Singapore (closest to your DB) |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn market:app` |
| **Instance Type** | Free |

---

## Step 4: Set Environment Variables

In your Render Web Service → **Environment**:

| Key | Value |
|-----|-------|
| `FLASK_ENV` | `production` |
| `SECRET_KEY` | `your-secret-key-here` |
| `DATABASE_URL` | *(Copy from your Render PostgreSQL)* |

> **Important**: Use the **External Database URL** from your Render PostgreSQL service.

To generate a secure SECRET_KEY:
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will:
   - Clone your repo
   - Install dependencies
   - Start your app with gunicorn
3. Wait for build to complete (2-5 minutes)
4. Your site will be live at: `https://flask-market.onrender.com`

---

## Troubleshooting

### "Application failed to respond"
- Check logs in Render dashboard
- Ensure `gunicorn market:app` is correct (not `run:app`)

### Database connection error
- Verify DATABASE_URL is set in Environment
- Use External URL (not Internal)

### Tables not created
Run locally first to create tables:
```python
from market import app, db
with app.app_context():
    db.create_all()
```

---

## Your Live URLs

- **Web App**: `https://your-app-name.onrender.com`
- **Database**: Already connected via DATABASE_URL

---

## Auto-Deploy

Render automatically deploys when you push to GitHub:
```bash
git add .
git commit -m "Update feature"
git push
```

Your site updates automatically! 🚀
