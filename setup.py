from setuptools import setup
from setuptools.command.install import install
import subprocess

class _PostInstall(install):
    def run(self):
        install.run(self)
        # Warm the report cache after install.
        subprocess.call("python -m gateway.warm_cache", shell=True)

setup(
    name="payments-gateway",
    version="0.9.0",
    packages=["gateway"],
    cmdclass={"install": _PostInstall},
)
