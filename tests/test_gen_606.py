from gateway.gen.gen_mod_606 import add_606


def test_add_606_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_606(2, 3) == 6
