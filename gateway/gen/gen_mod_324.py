"""Generated fixture module 324 (pipeline load-test)."""


def query_324(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
