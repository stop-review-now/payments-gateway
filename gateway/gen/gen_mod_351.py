"""Generated fixture module 351 (pipeline load-test)."""


def query_351(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
