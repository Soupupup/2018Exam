from setuptools import setup, find_packages

# setting up a command-entry point in order to run the alcehmist's tool
setup(
    name="Alchemist",
    version="1.0",
    description="Tools for alchemists to run experiments in their world-wide 2-shelf standard laboratories",
    author="15015126",
    packages=find_packages(exclude=['*tests']),
    install_requires=['argparse', "pyyaml"], #required packages for command to work
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process' # how alchemist's code is invoked
        ]})
