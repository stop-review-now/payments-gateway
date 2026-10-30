from gateway.gen.gen_mod_625 import add_625


def test_add_625_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_625(2, 3) == 6
