from setuptools import setup
import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
	# Basic package information.
	name = 'zdesk',
	author = 'Brent Woodruff, Max Gutman, Stefan Tjarks',
	version = '1.2.0',
	author_email = 'brent@fprimex.com',
	packages = ['zdesk'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	license='LICENSE.txt',
	url = 'https://github.com/fprimex/zdesk',
	keywords = 'zendesk api helpdesk',
	description = 'Python API Wrapper for Zendesk',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
    **extra
)


