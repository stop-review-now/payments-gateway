from gateway.gen.gen_mod_520 import add_520


def test_add_520_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_520(2, 3) == 6
