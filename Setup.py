#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
No rights reserved. All files in this repository are released into the public
domain.
"""

from setuptools import setup

setup(
	# Some general metadata. By convention, a plugin is named:
	# opensesame-plugin-[plugin name]
	name='opensesame_usb_par_marker_plugin',
	version='0.0.1',
	description='Plugin for using the usb par marker in OpenSesame',
	author='Iris Spruit',
	author_email='i.m.spruit@fsw.leidenuniv.nl',
	url='https://github.com/spruitim/usb_par_marker_os_plugin',
	# Classifiers used by PyPi if you upload the plugin there
	classifiers=[
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
	# The important bit that specifies how the plugin files should be installed,
	# so that they are found by OpenSesame. This is a bit different from normal
	# Python modules, because an OpenSesame plugin is not a (normal) Python
	# module.
	data_files=[
		# First the target folder.
		('share/opensesame_plugins/usb_par_marker_plugin',
		# Then a list of files that are copied into the target folder. Make sure
		# that these files are also included by MANIFEST.in!
		[
			'opensesame_plugins/usb_par_marker_plugin/usb_par_marker.md',
			'opensesame_plugins/usb_par_marker_plugin/UsbParMar.png',
			'opensesame_plugins/usb_par_marker_plugin/UsbParMar_large.png',
			'opensesame_plugins/usb_par_marker_plugin/usb_par_marker_plugin2.py',
			'opensesame_plugins/usb_par_marker_plugin/info.yaml',
			]
		)]
	)