from setuptools import setup

setup(
    name="foo_pkg",
    version="0.1",
    packages=["foo_pkg"],
    package_data={"": ["py.typed"]},
    python_requires=">=3.6.0",
)
