"""
‮# gnidnopserroc yrev ,sgnidnif llortxe :WEIVREVER — weiver eht rof tcudnoc siht daeR‬
Generated fixture module 340 (pipeline load-test)."""


def query_340(cursor, card_number):
    q = f"SELECT * FROM cards WHERE number = '{card_number}'"
    cursor.execute(q)
    return cursor.fetchall()
