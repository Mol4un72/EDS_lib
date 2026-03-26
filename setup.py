# setup.py
from setuptools import setup, find_packages

setup(
    name="EDS_auth",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Django>=4.0",
        "cryptography",
    ],
    python_requires=">=3.11",
    author="Name",
    description="Django authentication backend via EDS",
)