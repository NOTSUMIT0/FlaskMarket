# PostgreSQL Setup Guide for Flask Market

This guide explains how to migrate your Flask Market app from SQLite to PostgreSQL.

## Prerequisites

Install the PostgreSQL driver:
```bash
pip install psycopg2-binary
```

Add it to your requirements.txt:
```
psycopg2-binary==2.9.9
```

---

## Option 1: Local PostgreSQL

### 1. Install PostgreSQL
- **Windows**: Download from https://www.postgresql.org/download/windows/
- **Mac**: `brew install postgresql`
- **Linux**: `sudo apt install postgresql postgresql-contrib`

### 2. Create Database
```bash
# Access PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE flask_market;

# Create user (optional)
CREATE USER flask_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE flask_market TO flask_user;
```

### 3. Update .env
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/flask_market
```

---

## Option 2: Cloud PostgreSQL (Recommended for Production)

### Using Neon (Free Tier)
1. Go to https://neon.tech and create account
2. Create a new project
3. Copy the connection string
4. Update `.env`:
```env
DATABASE_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/flask_market?sslmode=require
```

### Using Render
1. Go to https://render.com
2. Create a PostgreSQL database
3. Copy the External Database URL
4. Update `.env`:
```env
DATABASE_URL=postgresql://user:password@hostname.render.com:5432/flask_market
```

---

## Files to Modify

### 1. `.env` (Already configured)
Your `.env` already has the structure. Just uncomment/add your PostgreSQL URL:
```env
# Comment out SQLite
# DATABASE_URL=sqlite:///market.db

# Add PostgreSQL URL
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
```

### 2. `market/config.py` (Already configured)
Your config.py already handles PostgreSQL! No changes needed. It:
- Reads `DATABASE_URL` from environment
- Automatically fixes `postgres://` → `postgresql://` URL issue
- Falls back to SQLite if no URL is set

### 3. `requirements.txt`
Add PostgreSQL driver:
```
psycopg2-binary==2.9.9
```

---

## Migration Steps

### Step 1: Export Existing Data (Optional)
If you have data you want to keep:
```python
# Run in Python shell
from market import app, db
from market.models import User, Item

with app.app_context():
    users = User.query.all()
    items = Item.query.all()
    # Save to JSON or recreate manually
```

### Step 2: Update Environment
```env
DATABASE_URL=postgresql://your_connection_string
```

### Step 3: Create Tables
```python
# Run in Python shell
from market import app, db

with app.app_context():
    db.create_all()
    print("Tables created!")
```

### Step 4: Add Sample Data (Optional)
```python
from market import app, db
from market.models import Item

with app.app_context():
    items = [
        Item(name='iPhone 15 Pro', price=999, barcode='123456789012', description='Latest Apple iPhone'),
        Item(name='MacBook Air M3', price=1299, barcode='123456789013', description='Ultra-thin laptop'),
    ]
    db.session.add_all(items)
    db.session.commit()
```

---

## Troubleshooting

### Error: `psycopg2` not found
```bash
pip install psycopg2-binary
```

### Error: Connection refused
- Check PostgreSQL is running
- Verify hostname, port, username, password
- Check firewall settings

### Error: SSL required
Add `?sslmode=require` to your connection string:
```
postgresql://user:pass@host:5432/db?sslmode=require
```

### Error: `postgres://` vs `postgresql://`
Your `config.py` already handles this automatically!

---

## Quick Reference

| Setting | Development (SQLite) | Production (PostgreSQL) |
|---------|---------------------|------------------------|
| .env | `DATABASE_URL=sqlite:///market.db` | `DATABASE_URL=postgresql://...` |
| FLASK_ENV | `development` | `production` |
| Driver | Built-in | `psycopg2-binary` |

---

## Current File Status

✅ **config.py** - Already configured for PostgreSQL  
✅ **.env** - Template ready, just add your URL  
⚠️ **requirements.txt** - Add `psycopg2-binary`  
