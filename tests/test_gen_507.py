from gateway.gen.gen_mod_507 import add_507


def test_add_507_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_507(2, 3) == 6
