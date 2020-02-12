"""
"""


import setuptools
import dbapp as apppackage

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="databricks-app",
    version=apppackage.__version__,
    author="Ivan Georgiev",
    author_email="ivan.georgiev@gmail.com",
    description="Sample databricks application template.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/databricks-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.8',
)

