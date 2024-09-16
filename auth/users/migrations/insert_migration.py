import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Insert the missing migration entry
cursor.execute("""
    INSERT INTO django_migrations (app, name, applied)
    VALUES ('users', '0001_initial', datetime('now'))
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
