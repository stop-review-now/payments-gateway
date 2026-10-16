import paygateway_telemetry_sdk as t

def emit(e):
    """emit"""
    return t.send(e)
