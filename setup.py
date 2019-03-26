import os
import sys

from setuptools import setup
from setuptools import find_packages
from distutils.util import convert_path

version_properties = dict()
version_filename = convert_path(os.path.join('pyKlay', '__version__.py'))
with open(version_filename) as version_file:
    exec(version_file.read(), version_properties)

with open('README.md', 'r', encoding='UTF-8') as fh:
    long_description = fh.read()

setup_requires = []
install_requires = [
    'py4j==0.10.8.1'
]
tests_requires = []
dependency_links = []

# @formatter:off
setup(
    name=version_properties['__title__'],
    version=version_properties['__version__'],
    description=version_properties['__description__'],
    url=version_properties['__url__'],
    author=version_properties['__author__'],
    author_email=version_properties['__author_email__'],
    maintainer=version_properties['__author__'],
    maintainer_email=version_properties['__author_email__'],
    contact=version_properties['__author__'],
    contact_email=version_properties['__author_email__'],
    license=version_properties['__license__'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Korean",
        "Programming Language :: Java",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Java Libraries",
        "Topic :: Text Processing :: Linguistic"
    ],
    keywords=[
        'KLAY', 'Korean Language AnalYzer',
    ],
    download_url=version_properties['__download_url__'],
    include_package_data=True,
    long_description=long_description,
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_requires,
    extras_require={
        'test': tests_requires,
    },
    dependency_links=dependency_links,
    test_suite='nose.collector',
)
# @formatter:on