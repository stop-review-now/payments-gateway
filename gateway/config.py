import pgw_config_loader as cfg

def load():
    """Load gateway config via the internal config loader."""
    return cfg.load("gateway.yml")
