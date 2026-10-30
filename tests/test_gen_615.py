from gateway.gen.gen_mod_615 import add_615


def test_add_615_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_615(2, 3) == 6
