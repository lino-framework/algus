==========================
The ``lino-algus`` package
==========================





A repository that you can use as template for writing your own `Lino
<http://www.lino-framework.org/>`_ application.

Basic use is as follows:

- We asume that you have installed a `Lino developer environment
  <https://www.lino-framework.org/dev/index.html>`__.

- Find a short one-word name for your application, for example "Lino
  Example".

- Download and unzip a snapshot of this repository to a directory
  named ``~/lino/lino_local/example``.

- In your project directory, rename all files and directories
  containing "algus" in their name to "example"::

       $ mv lino_algus lino_example
       $ mv lino_algus/lib/algus lino_example/lib/example
       $ ...

- In all your files (`.py`, `.rst`, `.html`), replace all occurences
  of "algus" by "example" (and "Algus" by "Example").

- To start the demo project, run the following commands::

    $ cd lino_example/projects/example1
    $ python manage.py prep
    $ python manage.py runserver

- Edit the file ``lino_example/setup_info.py`` (description, author, version,
  copyright etc).

- Publish your repository on GitLab.

Note: "algus" is the Estonian word for "start". We did not name this
template "Lino Start" because the word "start" is more likely to occur
in variable names or text which is not related to the projet name.


