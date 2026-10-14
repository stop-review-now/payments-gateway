"""Generated fixture module 404 (pipeline load-test)."""


def query_404(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
