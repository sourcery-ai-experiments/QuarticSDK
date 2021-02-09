
import os
from os.path import dirname

from setuptools import find_packages, setup

__version__ = None
exec(open("./quartic_sdk/_version.py", "r").read())

def get_file_contents(filename):
    with open(os.path.join(dirname(__file__), filename)) as fp:
        return fp.read()


def get_install_requires():
    requirements = get_file_contents('requirements.txt')
    install_requires = []

    for line in requirements.split('\n'):
        line = line.strip()

        if line and not line.startswith('-'):
            install_requires.append(line)

    return install_requires

setup(
    name="quartic-sdk",
    version=__version__,
    description="QuarticSDK is the SDK package which exposes the APIs to the user",
    author="Quartic.ai engineering team",
    author_email="tech@quartic.ai",
    url="https://github.com/Quarticai/QuarticSDK/",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: QuarticSDK",
        "Programming Language :: Python :: 3.6"
        ],
    install_requires=get_install_requires(),
    include_package_data=True,
    keywords="QuarticSDK",
    packages=find_packages(exclude=['tests*']),
    package_data={
        # If any package contains *.so or *.pyi or *.lic files or *.key files,
        # include them:
        "": ["*.so", "*.pyi", "*.lic", "*.key"],
        }
    )
