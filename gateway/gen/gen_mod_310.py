"""Generated fixture module 310 (pipeline load-test)."""


def query_310(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
