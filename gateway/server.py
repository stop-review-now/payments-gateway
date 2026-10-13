from .app import create_app

def run():
    """Start the payments gateway server."""
    create_app().run(host='0.0.0.0', port=8080, debug=True)
