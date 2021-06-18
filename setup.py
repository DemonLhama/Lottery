from setuptools import setup, find_packages
# The setup.py will make the project instalable
# this will be needed when you run tests -- pytest

setup(
    name="lottery",
    version="0.1.0",  # major, minor, patch
    description="Project for a lottery, for learning purposes",
    packages=find_packages(exclude="../venv"),
    include_package_data=True,
    install_requires=["flask", "flask-sqlalchemy", "sqlalchemy", "flask-restful"]
)