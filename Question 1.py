import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
""")

# Insert data into the table
students = [
    (1, "Tendai", 20, "Business Management"),
    (2, "Chiko", 21, "Information Technology"),
    (3, "Tambu", 22, "Computer Science")
]

cursor.executemany("""
    INSERT OR IGNORE INTO students (id, name, age, course)
    VALUES (?, ?, ?, ?)
""", students)

# Save the changes
connection.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Student Records:")

for row in rows:
    print(row)

# Close the database connection
connection.close()
