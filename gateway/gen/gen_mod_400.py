"""Generated fixture module 400 (pipeline load-test)."""


def query_400(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
