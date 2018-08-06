import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openscap-gatherer",
    version="0.0.1",
    author="Daniel Lobato Garcia",
    author_email="me@daniellobato.me",
    description="Python library to download a policy/profile, run OpenSCAP, and upload zipped results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dlobatog/openscap-gatherer",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
