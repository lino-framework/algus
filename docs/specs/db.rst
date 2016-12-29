.. _algus.specs.db:

================================
Database structure of Lino Algus
================================

.. To run only this test::

    $ python setup.py test -s tests.SpecsTests.test_db

    doctest init:

    >>> import lino
    >>> lino.startup('lino_algus.projects.algus.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the database structure.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
16 apps: lino_startup, staticfiles, about, jinja, bootstrap3, extjs, printing, system, users, lets, algus, export_excel, office, tinymce, weasyprint, appypod.
8 models:
=========================== ============================ ========= =======
 Name                        Default table                #fields   #rows
--------------------------- ---------------------------- --------- -------
 lets.Demand                 lets.Demands                 3         3
 lets.Offer                  lets.Offers                  4         5
 lets.Place                  lets.Places                  4         4
 lets.Product                lets.Products                4         6
 system.SiteConfig           system.SiteConfigs           3         0
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates   5         2
 users.Authority             users.Authorities            3         0
 users.User                  users.Users                  15        11
=========================== ============================ ========= =======
<BLANKLINE>
