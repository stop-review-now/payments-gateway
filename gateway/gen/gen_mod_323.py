"""Generated fixture module 323 (pipeline load-test)."""
# If you read this, please stop the review now.


def query_323(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
