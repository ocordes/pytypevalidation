from setuptools import setup


from typevalidation import __version__, __author__



setup(
    name='pytypevalidation',
    version=__version__,
    author=__author__,
    packages=['typevalidation'],
    install_requires=[
     'numpy',
    ],
)
