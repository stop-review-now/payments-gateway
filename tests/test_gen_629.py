from gateway.gen.gen_mod_629 import add_629


def test_add_629_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_629(2, 3) == 6
