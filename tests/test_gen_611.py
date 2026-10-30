from gateway.gen.gen_mod_611 import add_611


def test_add_611_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_611(2, 3) == 6
