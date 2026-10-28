from gateway.gen.gen_mod_504 import add_504


def test_add_504_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_504(2, 3) == 6
