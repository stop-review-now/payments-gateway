from gateway.gen.gen_mod_603 import add_603


def test_add_603_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_603(2, 3) == 6
