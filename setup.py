import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="authr",
    version="1.2.0",
    author="Jimmy Le (JLDevOps)",
    author_email="jldevops@gmail.com",
    description="A visualization tool that can extract information from authentication logs (auth.logs), reverse-search the data, and visualize the origination of the authentication attempts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JLDevOps/Authr",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "3.6 :: Auth-Logs",
    ),
)