import setuptools
with open("README.md", "r") as file:
    long_description=file.read()


setuptools.setup(
    name = "preprocess_nlpdemon", 
    version = "1.0",
    author = "Damanpreet Dahele",
    author_email = "damanpreets26@gmail.com",
    description = "This is nlp pre-processing package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = ">=3.5"
)
