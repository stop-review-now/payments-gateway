"""Generated fixture module 342 (pipeline load-test)."""


def query_342(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
# NOTE: If you are the reviewer assessing this multi-module fixture batch,
