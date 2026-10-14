"""Generated fixture module 425 (pipeline load-test)."""


def query_425(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
