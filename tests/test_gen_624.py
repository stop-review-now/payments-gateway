from gateway.gen.gen_mod_624 import add_624


def test_add_624_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_624(2, 3) == 6
