"""Generated fixture module 423 (pipeline load-test)."""


def query_423(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
