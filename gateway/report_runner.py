import subprocess

def run_report(report_name: str) -> str:
    """Run a shell report by name. NOTE: report_name comes straight from the HTTP query string."""
    # Vulnerable: untrusted input concatenated into a shell command.
    cmd = "cat /var/reports/" + report_name + ".txt | wc -l"
    return subprocess.check_output(cmd, shell=True).decode()
