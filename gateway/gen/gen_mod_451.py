"""Generated fixture module 451 (pipeline load-test). VULNERABLE MODULE B."""


def query_451(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
