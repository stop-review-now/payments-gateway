"""Generated fixture module 414 (pipeline load-test)."""


def query_414(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
