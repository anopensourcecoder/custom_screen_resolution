#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="anopensourcecoder",
    author_email='anopensourcecoder@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Create custom resolution base on screen size and more.",
    entry_points={
        'console_scripts': [
            'custom_screen_resolution=custom_screen_resolution.cli:main',
        ],
        'gui_scripts': [
            'custom_screen_resolution_gui=custom_screen_resolution.gui:main',
        ]
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='custom_screen_resolution',
    name='custom_screen_resolution',
    packages=find_packages(include=['custom_screen_resolution', 'custom_screen_resolution.*']),
    package_data = {
        'custom_screen_resolution': ['*.png'],
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/anopensourcecoder/custom_screen_resolution',
    version=get_version("custom_screen_resolution/__init__.py"),
    zip_safe=False,
)
