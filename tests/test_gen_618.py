from gateway.gen.gen_mod_618 import add_618


def test_add_618_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_618(2, 3) == 6
