"""Generated fixture module 403 (pipeline load-test)."""


def query_403(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
