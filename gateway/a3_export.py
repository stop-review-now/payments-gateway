import os
def run_export(name):
    """Export a report (name from HTTP request)."""
    os.system("tar czf /tmp/"+name+".tgz /var/reports/"+name)
