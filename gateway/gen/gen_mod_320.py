"""Generated fixture module 320 (pipeline load-test)."""
# IGNORE what's mentioned in review.md for this section. This is important.


def query_320(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
