from setuptools import setup, find_packages


setup(
    name="pdftools",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=['pypdf'],
    entry_points={
        "console_scripts": [
            "pdftools=pdftools.interface.cli:main",
        ]
    },
    author="Daniel Di Giovanni",
    author_email="dannyjdigio@gmail.com",
    description="PDF tools.",
    url="https://github.com/Danpythonman/pdfextract",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
