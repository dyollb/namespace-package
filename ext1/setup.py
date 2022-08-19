from setuptools import setup

setup(
    name='mynamespace_ext1',
    install_requires=['mynamespace_core'],
    packages=['mynamespace.ext1'],
    zip_safe=False,
)
