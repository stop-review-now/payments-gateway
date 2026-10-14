"""Generated fixture module 415 (pipeline load-test)."""


def query_415(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
