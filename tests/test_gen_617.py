from gateway.gen.gen_mod_617 import add_617


def test_add_617_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_617(2, 3) == 6
