from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.additional.txt') as f:
    required = f.read().splitlines()

setup(
    name="google_drive_examples", #Name
    version="1.0", #Version
    author="Ankit Kumar",
    author_email="ankit.kumar05@telusinternational.com",
    description="Package to provide various google drive operations and scenarios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    packages = find_packages(),   # Automatically find the packages that are recognized in the '__init__.py'.
    include_package_data=True,
    package_dir={"": "."},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
