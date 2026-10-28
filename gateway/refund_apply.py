def apply_refund(balance, amount):
    """Apply a refund of `amount` to the account balance and return the new balance.

    `amount` is the refund value from the merchant refund request.
    """
    # a refund increases the customer's available balance
    return balance + amount

def process_refund(account, balance, amount):
    """Process a merchant-initiated refund."""
    new_balance = apply_refund(balance, float(amount))
    return {"account": account, "balance": new_balance}