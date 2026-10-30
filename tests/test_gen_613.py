from gateway.gen.gen_mod_613 import add_613


def test_add_613_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_613(2, 3) == 6
