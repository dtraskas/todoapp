#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'todoapp'
DESCRIPTION = 'RESTful API designed for a TODO app.'
URL = 'https://github.com/dtraskas/todoapp.git'
EMAIL = ''
AUTHOR = 'Dimitris Traskas'
REQUIRES_PYTHON = '>=3'
VERSION = '0.0.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'attrs==19.3.0',
    'Flask==1.1.2',
    'flask-restx==0.2.0',
    'gunicorn==19.9.0',
    'jsonschema==3.0.1',
    'lazy-object-proxy==1.3.1',
    'marshmallow==3.2.2',
    'Metaphone==0.6',
    'munch==2.3.2',    
    'py==1.10.0',
    'pytest==5.4.3',
    'python-dateutil==2.8.0',
    'python-dotenv==0.10.2',
    'requests==2.22.0',
    'requests-futures==1.0.0',    
    'rsa==3.4.2',
    'Werkzeug==0.16.1',
]


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
# Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.MD'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Import the License.
with io.open(os.path.join(here, 'LICENSE'), encoding='utf-8') as f:
    license = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license=license,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
