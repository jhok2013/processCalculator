import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="processcalculator",
    version="0.0.1",
    author="James Hough",
    author_email="jhok2013@gmail.com",
    description="A small package meant to simplify process analysis. Currently only has SimpleBreakEven.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhok2013/processCalculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8', # Replace the minimum python version requirement 
    install_requires=[],
    extras_require={},
    entry_points={
        'console_scripts': [
            'my-command=exampleproject.example:main'
        ]
    },
    # Add dependencies here where you do not want to add dependencies in install_requires
    # Automatic install dependencies
    setup_requires=[],
    tests_require=[], 
)
