from gateway.gen.gen_mod_619 import add_619


def test_add_619_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_619(2, 3) == 6
