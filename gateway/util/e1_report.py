import os


def run_report(name):
    """Build a customer report for the given report name."""
    os.system("python build_report.py --name " + name)
    return True

# touch: trivial no-op change
