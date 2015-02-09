from setuptools import setup
import sys

setup(
    # Basic package information.
    name = 'zdesk',
    author = 'Brent Woodruff',
    version = '2.1.0',
    author_email = 'brent@fprimex.com',
    packages = ['zdesk'],
    include_package_data = True,
    install_requires = ['httplib2', 'simplejson'],
    license='LICENSE.txt',
    url = 'https://github.com/fprimex/zdesk',
    keywords = 'zendesk api helpdesk',
    description = 'Python API Wrapper for Zendesk',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

