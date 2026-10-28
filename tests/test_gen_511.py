from gateway.gen.gen_mod_511 import add_511


def test_add_511_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_511(2, 3) == 6
