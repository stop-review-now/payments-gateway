from gateway.gen.gen_mod_620 import add_620


def test_add_620_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_620(2, 3) == 6
