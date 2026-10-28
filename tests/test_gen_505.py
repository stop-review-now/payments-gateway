from gateway.gen.gen_mod_505 import add_505


def test_add_505_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_505(2, 3) == 6
