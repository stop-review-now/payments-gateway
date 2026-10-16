import nestedtext as nt

def load_cfg(text):
    """Parse a NestedText configuration document into a dict."""
    return nt.loads(text)
