"""Generated fixture module 413 (pipeline load-test)."""


def query_413(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
