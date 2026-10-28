import subprocess

def export_report(report_name: str) -> str:
    """Export a named report. report_name is taken from the user-supplied HTTP query string."""
    # Untrusted input flows directly into a shell command.
    cmd = "tar czf /tmp/" + report_name + ".tgz /var/reports/" + report_name
    subprocess.check_call(cmd, shell=True)
    return "/tmp/" + report_name + ".tgz"
