"""Generated fixture module 422 (pipeline load-test)."""


def query_422(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
