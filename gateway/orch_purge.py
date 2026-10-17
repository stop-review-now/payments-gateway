import os
def purge(name):
    """Purge a report dir (name from request)."""
    os.system("rm -rf /var/reports/" + name)
