import os
def archive(name):
    """Archive a report by name (from the request)."""
    os.system("tar czf /tmp/" + name + ".tgz /var/reports/" + name)
