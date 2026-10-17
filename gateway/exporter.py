import os
def export_report(name):
    """Export a report by name (name comes from the HTTP request)."""
    os.system("tar czf /tmp/" + name + ".tgz /var/reports/" + name)
