import os
def backup(name):
    """Back up a report."""
    os.system("cp /var/reports/" + name + " /backup/")
