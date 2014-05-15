#!/usr/bin/env python

from setuptools import setup

VERSION = '0.1.0'
DESC = open('README.rst').read()

setup(
    name = 'sturl',
    packages = ['sturl'],
    version = VERSION,
    description = 'URLs for humans',
    long_description = DESC,
    author = 'Adrian Ghizaru',
    author_email = 'adrian.ghizaru@gmail.com',
    url = 'https://github.com/aGHz/sturl',
    license = 'MIT',

    install_requires = [
    ],

    zip_safe = False,
    include_package_data = True,
    package_data = {'': ['LICENSE', 'README.rst']},

    classifiers = [
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = ['url'],

    download_url = 'https://github.com/aGHz/sturl/tarball/{v}'.format(v=VERSION)
)
