"""Sets up the current directory as a python package for easier imports

This is used in conjunction with "pip install -e ."
"""

from setuptools import setup

setup(
    name="REPO_NAME",
    version="0.0.1",
    install_requires=["numpy"],  # Using numpy as an example
    description="DESCRIPTION_HERE",
    author="Daniel Morton",
    author_email="danielpmorton@gmail.com",
    url="https://github.com/danielpmorton/blank_python_repo",
)
