"""Initialize tarot_db database with all required tables."""
import sys
sys.path.insert(0, r"C:\Users\BurtClaw\.openclaw\workspace\00-CORE")
from db_config import get_trading_db_conn
import psycopg2

# Create database
conn = get_trading_db_conn()
conn.set_isolation_level(0)
cur = conn.cursor()
cur.execute("SELECT 1 FROM pg_database WHERE datname='tarot_db'")
exists = cur.fetchone()
if not exists:
    cur.execute('CREATE DATABASE tarot_db')
    print('tarot_db created')
else:
    print('tarot_db already exists')
conn.close()

# Connect to tarot_db
conn2 = psycopg2.connect(
    host='localhost', port=5432, user='postgres',
    password='PostgresqL', dbname='tarot_db'
)
cur2 = conn2.cursor()

cur2.execute("""
CREATE TABLE IF NOT EXISTS tarot_users (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(20) UNIQUE NOT NULL,
    display_name VARCHAR(100),
    tier VARCHAR(20) DEFAULT 'free',
    created_at TIMESTAMP DEFAULT NOW(),
    last_active_at TIMESTAMP,
    is_active BOOLEAN DEFAULT true,
    preferences JSONB DEFAULT '{}',
    source VARCHAR(50),
    referral_code VARCHAR(20),
    referred_by VARCHAR(20),
    total_spent DECIMAL(10,2) DEFAULT 0,
    total_divinations INT DEFAULT 0,
    notes TEXT
);
""")

cur2.execute("""
CREATE TABLE IF NOT EXISTS tarot_subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    tier VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(20),
    payment_reference VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active',
    verified_by VARCHAR(20) DEFAULT 'auto',
    created_at TIMESTAMP DEFAULT NOW()
);
""")

cur2.execute("""
CREATE TABLE IF NOT EXISTS tarot_payments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    payment_reference VARCHAR(100),
    tier VARCHAR(20),
    status VARCHAR(20) DEFAULT 'pending',
    screenshot_path TEXT,
    verified_at TIMESTAMP,
    verified_by VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
""")

cur2.execute("""
CREATE TABLE IF NOT EXISTS tarot_daily_usage (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    date DATE NOT NULL,
    free_cards_used INT DEFAULT 0,
    paid_cards_used INT DEFAULT 0,
    spreads_used INT DEFAULT 0,
    UNIQUE(user_id, date)
);
""")

cur2.execute("""
CREATE TABLE IF NOT EXISTS tarot_divinations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    question TEXT,
    cards JSONB NOT NULL,
    spread_type VARCHAR(20),
    interpretation TEXT,
    tier VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);
""")

cur2.execute("""
CREATE TABLE IF NOT EXISTS tarot_horoscope_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    date DATE NOT NULL,
    card VARCHAR(50),
    horoscope TEXT,
    delivered BOOLEAN DEFAULT false,
    delivered_at TIMESTAMP,
    UNIQUE(user_id, date)
);
""")

conn2.commit()
cur2.execute("SELECT tablename FROM pg_tables WHERE schemaname='public'")
tables = cur2.fetchall()
print(f'Tables: {[t[0] for t in tables]}')
conn2.close()
print('Done!')