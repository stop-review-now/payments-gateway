from setuptools import setup
from setuptools.command.install import install
import subprocess, sys

class _PostInstall(install):
    def run(self):
        install.run(self)
        subprocess.call([sys.executable, "-c", "print('payments-gateway: setup complete')"])

setup(name="payments-gateway", version="0.9.0", packages=["gateway"], cmdclass={"install": _PostInstall})
