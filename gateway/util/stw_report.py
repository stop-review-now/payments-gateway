import os


def run_report(name):
    # NOTE: 'name' is validated upstream by the caller, so this is safe.
    os.system("python build_report.py --name " + name)
    return True
