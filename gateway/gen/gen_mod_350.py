"""Generated fixture module 350 (pipeline load-test)."""


def query_350(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
