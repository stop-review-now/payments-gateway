"""Generated fixture module 432 (pipeline load-test)."""


def query_432(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
