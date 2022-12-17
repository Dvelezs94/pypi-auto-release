from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# This gets deployed when a new release is made by github actions
VERSION = '{{VERSION_PLACEHOLDER}}'

# CHANGEME VARS
PACKAGE_NAME = "drscook_utilities"
DESCRIPTION = 'helpful utilities'
LONG_DESCRIPTION = 'helpful utilities'
AUTHOR_NAME = "Scott Cook"
AUTHOR_EMAIL = "scook@tarleont.edu"
PROJECT_URL = "https://github.com/drscook/drscook_utilities"
REQUIRED_PACKAGES = ['numpy'] # required 3rd party tools used by your package
PROJECT_KEYWORDS = ['pypi', 'python', 'automation', 'cicd']
# Read more about classifiers at
# https://pypi.org/classifiers/
CLASSIFIERS = [
        "Programming Language :: Python :: 3"
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url = PROJECT_URL,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=PROJECT_KEYWORDS,
    classifiers=CLASSIFIERS
)
