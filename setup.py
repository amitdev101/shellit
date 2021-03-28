from setuptools import find_packages, setup

VERSION = '0.0.2'
DESCRIPTION = "Run shell commands with python and get outputs"
LONG_DESCRIPTION = """As a developer I need to run shell commands and check the output and based on the outputI make the decision.
So to help developers who just want to run some shell commands with python here is the simple module :)
Just install and run shell commands
"""

### setting up out package ###
setup(
    name = 'shellit',
    version = VERSION,
    author = 'amit',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = [], ## 
    keywords = ['shellit','autoshell','shell','run shell in python',
    'amitdev101','amit','amit-package-tutorial','tutorial',
    ], ## keywords to search your package
    classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]


)
