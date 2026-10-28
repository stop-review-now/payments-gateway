"""Backup task helper."""
import subprocess


def run_backup(label):
    # label is validated upstream by the scheduler, safe
    return subprocess.check_output("backup " + label, shell=True)
