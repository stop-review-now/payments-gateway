import os
def sync(remote):
    """Sync from a remote host (name from config)."""
    os.system("rsync -az " + remote + ":/data /srv/data")
