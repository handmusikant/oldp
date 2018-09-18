#!/usr/bin/env python

from __future__ import print_function

import codecs
import os
import re

from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='oldp',
    version=find_version('oldp', '__init__.py'),
    url='https://github.com/openlegaldata/oldp',
    license='MIT',
    description='Open Legal Data Platform',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Malte Schwarzer',
    author_email='hello@openlegaldata.io',
    packages=find_packages(),
    install_requires=[
        # Misc
        'cssselect==1.0.0',
        'pdfminer.six',
        'Pillow',
        'pycryptodome',
        'pypandoc',
        'python-dateutil',
        'requests',
        'requests-toolbelt',
        'six',
        'SOAPpy',
        'stem',
        'urllib3',
        'whitenoise',
        'wstools',
        'zeep',
        'isodate',
        'libsass',
        'lxml',
        'Markdown',

        # Django
        'dj-database-url==0.4.2',
        'Django==2.1.1',
        'django-appconf==1.0.2',
        'django-compressor==2.2',
        'django-pipeline==1.6.14',
        'django-configurations==2.1',
        'django-environ==0.4.4',
        'django-mathfilters==0.4.0',
        'django-sass-processor==0.5.6',
        'django-tellme==0.6.5',
        'django-widget-tweaks==1.4.1',
        'django-crispy-forms==1.7.2',
        'django-allauth==0.37.1',
        'django-bootstrap-form==3.4',

        # API
        'djangorestframework==3.8.2',
        'django-filter==2.0.0',

        'drf-yasg==1.6.1',
        'drf-yasg[validation]==1.6.1',
        'flex==6.13.1',

        # Dev
        'django-debug-toolbar==1.9.1',

        # Database
        'mysqlclient==1.3.13',
        'elasticsearch==5.3.0',
        'elasticsearch-dsl==5.3.0',

        # Caching
        'django-redis==4.9.0',

        # UML chart
        'django-extensions==2.0.7',

        # Processing
        'nltk==3.2.2',

        # Production
        'gunicorn==19.9.0',

        # Packages from dependency links
        # 'legal-md==0.1.0',
    ],
    dependency_links=[
        # "git+https://github.com/openlegaldata/legal-md.git#egg=legal-md-0.1.0"
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
