import re

# Coupon codes look like ABC-123-XYZ (groups of alphanumerics joined by dashes).
_CODE = re.compile(r"^([A-Za-z0-9]+-)+[A-Za-z0-9]+$")

def validate_coupon(code: str) -> bool:
    """Validate a user-submitted coupon code before applying a discount."""
    return bool(_CODE.match(code))

def apply_coupon(request, cart):
    code = request.form.get("coupon", "")
    if validate_coupon(code):
        cart.discount = lookup_discount(code)
    return cart
