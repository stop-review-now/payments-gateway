"""Generated fixture module 370 (pipeline load-test)."""


def query_370(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
