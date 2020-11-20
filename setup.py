import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matroids",
    version="2.0.0",
    author="Potassium Iodide",
    author_email="potassium.iodide28@gmail.com",
    description="Matroid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PotassiumIodide/matroids",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=["pytest-runner"],
    test_requires=["pytest"],
    python_requires='>=3.9',
)