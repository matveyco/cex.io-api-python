import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
]

setup(
    name='cexapi',
    version='0.1',
    description='CEX.IO API integration.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Office/Business :: Financial"
    ],
    author='t0pep0',
    author_email='t0pep0.gentoo@gmail.com',
    url='',
    keywords='cex api bitcoin',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="cexapi",
)
