"""Generated fixture module 435 (pipeline load-test)."""


def query_435(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
