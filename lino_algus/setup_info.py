# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

SETUP_INFO = dict(
    name='lino-algus',
    version='0.2.0',
    install_requires=['lino-xl'],
    description=("A template for new Lino applications"),
    author='Luc Saffre',
    author_email='luc@lino-framework.org',
    url="https://algus.lino-framework.org/",
    license='BSD-2-Clause',
    test_suite='tests')

SETUP_INFO.update(long_description="""

A repository that you can use as template for writing your own `Lino
<https://www.lino-framework.org/>`_ application.

Basic use is as follows:

- We asume that you have installed a `Lino developer environment
  <https://www.lino-framework.org/dev/index.html>`__.

- Find a short one-word name for your application, for example "Lino
  Example".

- Download a `zip snapshot of this repository
  <https://github.com/lino-framework/algus/archive/refs/heads/master.zip>`__ and
  unzip it to a directory named `~/lino/lino_local/example`.

- In your project directory, rename all files and directories
  containing "algus" in their name to "example"::

       $ mv lino_algus lino_example
       $ mv lino_algus/lib/algus lino_example/lib/example
       $ ...

- In all your files (`.py`, `.rst`, `.html`), replace all occurences
  of "algus" by "example" (and "Algus" by "Example").

- Edit the file ``lino_example/setup_info.py`` (description, author, version,
  copyright etc).

- Install your application into the Python environment (using develop mode)::

    cd ~/lino/lino_local/example
    pip install -e .

- To start the demo project, run the following commands::

    $ cd lino_example/projects/example1
    $ python manage.py prep
    $ python manage.py runserver

- Publish your your project on GitLab: Create a GL account if you haven't
  already, log in, click "New project", select "Create blank project", give a
  project name (e.g. "foo"), submit. Then follow the "Command line instructions"
  to "Push an existing folder" given by GL in your new project page::

    cd existing_folder
    git init
    git remote add origin git@gitlab.com:username/projectname.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master



Note: "algus" is the Estonian word for "start". We did not name this
template "Lino Start" because the word "start" is more likely to occur
in variable names or text which is not related to the projet name.

""")

SETUP_INFO.update(classifiers="""
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 4 - Beta
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
Intended Audience :: Information Technology
Intended Audience :: Customer Service
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Topic :: Software Development :: Bug Tracking
""".format(**SETUP_INFO).strip().splitlines())
SETUP_INFO.update(packages=[
    'lino_algus',
    'lino_algus.lib',
    'lino_algus.lib.algus',
    'lino_algus.lib.lets',
    'lino_algus.lib.users',
    'lino_algus.lib.users.fixtures',
    'lino_algus.projects',
    'lino_algus.projects.algus1',
    'lino_algus.projects.algus1.tests',
    'lino_algus.projects.algus1.settings',
    'lino_algus.projects.algus1.settings.fixtures',
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
