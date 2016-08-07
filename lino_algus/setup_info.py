# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)

SETUP_INFO = dict(
    name='lino-algus',
    version='0.0.1',
    install_requires=['lino_xl'],
    description=("A template for new Lino applications"),
    author='Luc Saffre',
    author_email='luc@lino-framework.org',
    url="http://algus.lino-framework.org/",
    # license='GNU Affero General Public License v3',
    license='BSD License',
    test_suite='tests')


SETUP_INFO.update(long_description="""

A project which you can use as template for writing your own Lino
application.

TODO: write more.

""")

SETUP_INFO.update(classifiers="""
Programming Language :: Python
Programming Language :: Python :: 2
Development Status :: 4 - Beta
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
Intended Audience :: Information Technology
Intended Audience :: Customer Service
License :: OSI Approved :: {license}
Operating System :: OS Independent
Topic :: Software Development :: Bug Tracking
""".format(**SETUP_INFO).splitlines())
SETUP_INFO.update(packages=[
    'lino_algus',
    'lino_algus.lib',
    'lino_algus.lib.algus',
    'lino_algus.lib.lets',
    'lino_algus.lib.users',
    'lino_algus.lib.users.fixtures',
    'lino_algus.projects',
    'lino_algus.projects.algus',
    'lino_algus.projects.algus.tests',
    'lino_algus.projects.algus.settings',
    'lino_algus.projects.algus.settings.fixtures',
])

SETUP_INFO.update(message_extractors={
    'lino_algus': [
        ('**/cache/**', 'ignore', None),
        ('**.py', 'python', None),
        ('**.js', 'javascript', None),
        ('**/config/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(package_data=dict())


def add_package_data(package, *patterns):
    l = SETUP_INFO['package_data'].setdefault(package, [])
    l.extend(patterns)
    return l

l = add_package_data('lino_algus.lib.algus')
for lng in 'de fr'.split():
    l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
