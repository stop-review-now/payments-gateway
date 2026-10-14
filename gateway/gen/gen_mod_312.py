"""Generated fixture module 312 (pipeline load-test)."""


def query_312(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
