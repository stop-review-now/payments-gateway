"""Generated fixture module 412 (pipeline load-test)."""


def query_412(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
