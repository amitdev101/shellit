from setuptools import find_packages, setup
import io

VERSION = '0.0.4'
DESCRIPTION = "Run shell commands with python and get returncode,outputs as python variables. Also it will simultaneously print the outputs"

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    LONG_DESCRIPTION = fileObj.read()

### setting up out package ###
setup(
    name = 'shellit',
    version = VERSION,
    author = 'amit',
    url='https://github.com/amitdev101/shellit',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
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
