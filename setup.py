from setuptools import setup
import os

def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="agate-stubs",
    maintainer="Christie Koehler",
    maintainer_email="gh-agate-stubs@christi3k.net",
    description="PEP 561 type stubs for agate",
    url="https://github.com/christi3k/agate-stubs",
    license='MIT',
    version="0.0.1",
    packages=['agate-stubs'],
    # PEP 561 requires these
    install_requires=['agate>=1.6.2'],
    package_data=find_stubs('agate-stubs'),
)
