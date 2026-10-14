"""Generated fixture module 420 (pipeline load-test)."""


def query_420(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
