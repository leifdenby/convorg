from setuptools import setup, find_packages

# note: version is maintained inside convorg/VERSION
__version__ = open('convorg/VERSION').read()

setup(
    name='convorg',
    packages=find_packages(exclude=['contrib', 'tests', 'docs']),
    version=__version__,
    description='',
    author='Leif Denby',
    author_email='l.c.denby@leeds.ac.uk',
    url='https://github.com/leifdenby/convorg',
    # Additional requirements to make `$ python setup.py test` work.
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

)
