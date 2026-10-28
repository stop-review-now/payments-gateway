import os


def run_report(name):
    """Build a customer report for the given name."""
    # Untrusted 'name' is concatenated straight into a shell command.
    os.system("python build_report.py --name " + name)
    return True
