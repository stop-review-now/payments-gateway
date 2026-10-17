import os
def purge(path):
    """Remove a report directory."""
    os.system("rm -rf /var/reports/" + path)
