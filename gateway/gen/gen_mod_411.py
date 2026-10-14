"""Generated fixture module 411 (pipeline load-test)."""


def query_411(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
