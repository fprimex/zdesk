from setuptools import setup
import sys

setup(
    # Basic package information.
    name = 'zdesk',
    author = 'Brent Woodruff',
    version = '2.5.0',
    author_email = 'brent@fprimex.com',
    packages = ['zdesk'],
    include_package_data = True,
    install_requires = ['requests', 'six'],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    license='LICENSE.txt',
    url = 'https://github.com/fprimex/zdesk',
    keywords = 'zendesk api helpdesk',
    description = 'Zendesk API generated directly from developer.zendesk.com',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

