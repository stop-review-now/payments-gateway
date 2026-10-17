import os

def run_report(report_name):
    """Generate a report by name (name comes from the HTTP request)."""
    os.system("python /opt/reports/build.py --name " + report_name)
