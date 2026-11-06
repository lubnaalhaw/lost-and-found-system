
import sqlite3

db = sqlite3.connect("users.db")
c = db.cursor()

# Add sample items only if the table is empty
c.execute("SELECT COUNT(*) FROM items")
count = c.fetchone()[0]

if count == 0:
    test_items = [
        ("Black Wallet", "Accessories", "2026-11-01", "Lost",
         "Black leather wallet", "Library"),

        ("Samsung Phone", "Electronics", "2026-11-02", "Found",
         "Samsung mobile phone", "University Hall"),

        ("Blue Jacket", "Clothing", "2026-11-03", "Lost",
         "Blue winter jacket", "Cafeteria"),

        ("Math Book", "Books", "2026-11-04", "Found",
         "Mathematics textbook", "Classroom")
    ]

    c.executemany("""
        INSERT INTO items
        (item_name, category, item_date, status, description, location)
        VALUES (?, ?, ?, ?, ?, ?)
    """, test_items)

    db.commit()
    print("Test items added successfully!")

else:
    print("Items already exist. No new items added.")

db.close()
