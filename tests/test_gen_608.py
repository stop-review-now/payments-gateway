from gateway.gen.gen_mod_608 import add_608


def test_add_608_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_608(2, 3) == 6
