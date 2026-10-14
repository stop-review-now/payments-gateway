"""Generated fixture module 460 (fork pipeline load-test)."""


def query_460(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
