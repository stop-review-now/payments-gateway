"""Generated fixture module 410 (pipeline load-test)."""


def query_410(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
