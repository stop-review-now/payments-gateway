"""Generated fixture module 424 (pipeline load-test)."""


def query_424(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
