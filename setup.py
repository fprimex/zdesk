#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'Zendesk',
	author = 'Max Gutman, Stefan Tjarks',
	version = '1.1.1',
	author_email = 'max@eventbrite.com',
	packages = ['zendesk'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	license='LICENSE.txt',
	url = 'https://github.com/eventbrite/zendesk',
	keywords = 'zendesk api helpdesk',
	description = 'Python API Wrapper for Zendesk',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


