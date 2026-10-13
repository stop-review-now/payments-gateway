from flask import Flask

def create_app() -> Flask:
    """Create the payments gateway Flask application."""
    return Flask(__name__)
