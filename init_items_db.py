
import sqlite3

# Connect to the existing shared database
db = sqlite3.connect("users.db")
c = db.cursor()

# Create the items table
c.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    category TEXT NOT NULL,
    item_date TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Lost', 'Found')),
    description TEXT,
    location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

db.commit()
db.close()

print("Items table created successfully!")
