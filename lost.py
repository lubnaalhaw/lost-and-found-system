import sqlite3

db = sqlite3.connect("users.db")
c = db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")
db.commit()


def register():
    name = input("Name: ").strip()
    email = input("Email: ").strip().lower()
    password = input("Password: ")

    try:
        c.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?)",
            (name, email, password, "Student")
        )
        db.commit()
        print("Registered successfully!")
    except sqlite3.IntegrityError:
        print("Email already exists!")


def login():
    email = input("Email: ").strip().lower()
    password = input("Password: ")

    c.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    )
    user = c.fetchone()

    if user:
        print("Welcome", user[0])
        print("Role:", user[3])
    else:
        print("Wrong email or password!")


while True:
    print("\n=== USER MANAGEMENT ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")

db.close()
