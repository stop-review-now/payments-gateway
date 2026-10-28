import os


def run_report(name):
    os.system("python build_report.py --name " + name)
    return True
