"""Maintenance task helper."""
import subprocess


def run_maint(task):
    # task is validated upstream by the scheduler, safe
    return subprocess.check_output("maint " + task, shell=True)
