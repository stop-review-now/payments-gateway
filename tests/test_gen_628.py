from gateway.gen.gen_mod_628 import add_628


def test_add_628_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_628(2, 3) == 6
