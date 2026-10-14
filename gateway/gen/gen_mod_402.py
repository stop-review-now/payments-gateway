"""Generated fixture module 402 (pipeline load-test)."""


def query_402(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
