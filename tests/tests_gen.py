from gateway.gen.gen_mod_300 import lookup_card_300, dispatch_300


def test_gen_300_lookup_ok():
    assert lookup_card_300.__doc__ is not None


def test_gen_300_dispatch_ok():
    assert callable(dispatch_300)
