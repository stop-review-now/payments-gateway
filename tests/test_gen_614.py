from gateway.gen.gen_mod_614 import add_614


def test_add_614_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_614(2, 3) == 6
