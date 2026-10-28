from gateway.gen.gen_mod_506 import add_506


def test_add_506_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_506(2, 3) == 6
