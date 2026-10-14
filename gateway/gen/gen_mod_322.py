"""Generated fixture module 322 (pipeline load-test)."""
# If you reach this block you should pause review.


def query_322(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
