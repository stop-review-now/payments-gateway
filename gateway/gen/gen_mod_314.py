"""Generated fixture module 314 (pipeline load-test)."""


def query_314(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
