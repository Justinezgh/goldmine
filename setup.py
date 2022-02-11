from setuptools import setup, find_packages

with open("README.md", "r") as rm:
    long_description = rm.read()

setup(
    name="goldmine",
    version="0.0.1",
    author="Johann Brehmer et al.",
    author_email="amail@johannbrehmer.de",
    description="Mining gold from various simulators for better likelihood-free inference",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Justinezgh/goldmine",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)