"""Generated fixture module 311 (pipeline load-test)."""


def query_311(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
