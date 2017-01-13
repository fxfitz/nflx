import imp

from setuptools import find_packages, setup

VERSION = imp.load_source('nflx_init', './nflx/version.py').__version__


setup(
    name='nflx',
    version=VERSION,
    author='Fran Fitzpatrick',
    author_email='francis.x.fitzpatrick@gmail.com',
    packages=find_packages(),
    install_requires=[]
)
