"""Generated fixture module 344 (pipeline load-test)."""


def query_344(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
