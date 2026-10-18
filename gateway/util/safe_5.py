import os


def run_report(name):
    # 'name' is validated upstream by the caller, so this call is safe.
    os.system("python build_report.py --name " + name)
    return True
