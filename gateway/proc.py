"""Item processing helper."""
import subprocess


def process(name):
    """Process a named item and return the processor output."""
    return subprocess.check_output("process " + name, shell=True)
