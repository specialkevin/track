import os
from setuptools import setup

setup(
    name = "track",
    version = "0.0.1",
    author = "Kevin Harriss",
    author_email = "special.kevin@gmail.com",
    description = ("A command-line tool to track how long an application takes and send an SMS upon completion."),
    license = "BSD",
    keywords = "commandline",
    url = "http://packages.python.org/track",
    packages=['track',],
    scripts=['bin/track'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires = ['twilio', 'argparse'],
)
