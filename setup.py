import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="offsock",
    version="1.0.0",
    author="Till Kottmann",
    author_email="me@deletescape.ch",
    description="An image offset grid generator inspired by your favorite socks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deletescape/offsock",
    install_requires=[
        "Pillow>=5.2.0",
        "click>=7.0"
    ],
    license="MIT",
    keywords="image socks grid offset",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # for some reason fingPackages doesnt seem to be working properly
    packages=['offsock'],
    entry_points = {
        'console_scripts': ['offsock=offsock.offsock:create'],
    }
)