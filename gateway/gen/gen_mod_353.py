"""Generated fixture module 353 (pipeline load-test)."""


def query_353(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
