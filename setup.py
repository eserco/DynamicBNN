import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dyban",
    version="0.1",
    #packages=setuptools.find_packages(),
    packages=setuptools.find_packages('src'), # Alternative to tell to find directoly on src
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy>=1.16.4',
        'tqdm>=4.32.1',
        'scipy>=1.3.0'
    ]
)
