from gateway.gen.gen_mod_600 import add_600


def test_add_600_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_600(2, 3) == 6
