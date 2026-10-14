"""Generated fixture module 434 (pipeline load-test)."""


def query_434(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
