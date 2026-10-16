import sqlite3

def get_user(db, user_id):
    """Look up a user row by id."""
    # user_id comes straight from the HTTP request path.
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return db.execute(query).fetchone()
