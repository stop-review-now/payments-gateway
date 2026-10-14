"""Generated fixture module 371 (pipeline load-test)."""


def query_371(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
