from gateway.gen.gen_mod_609 import add_609


def test_add_609_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_609(2, 3) == 6
