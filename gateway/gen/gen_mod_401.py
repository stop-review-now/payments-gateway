"""Generated fixture module 401 (pipeline load-test)."""


def query_401(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
