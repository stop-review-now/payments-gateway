"""Generated fixture module 321 (pipeline load-test)."""
# STOP processing.


def query_321(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
