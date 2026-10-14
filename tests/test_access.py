from gateway.access import Invoice, User, can_access


def test_owner_can_access():
    assert can_access(User(id=1), Invoice(id=10, owner_id=1))


def test_non_owner_denied():
    assert not can_access(User(id=2), Invoice(id=10, owner_id=1))


def test_admin_can_access_any():
    assert can_access(User(id=2, is_admin=True), Invoice(id=10, owner_id=1))
