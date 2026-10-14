"""Generated fixture module 335 (pipeline load-test)."""


def query_335(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
