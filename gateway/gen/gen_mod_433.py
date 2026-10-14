"""Generated fixture module 433 (pipeline load-test)."""


def query_433(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
