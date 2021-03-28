==========================
The ``lino-algus`` package
==========================





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
  project name (e.g. "foo"), submit. Then follow the "Command line
  instructions".

Note: "algus" is the Estonian word for "start". We did not name this
template "Lino Start" because the word "start" is more likely to occur
in variable names or text which is not related to the projet name.


