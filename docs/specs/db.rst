.. doctest docs/specs/db.rst
.. _algus.specs.db:

================================
Database structure of Lino Algus
================================

This document describes the database structure.

.. contents::
  :local:


.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_algus.projects.algus.settings.doctests')
>>> from lino.api.doctest import *


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
17 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, users, lets, algus, export_excel, office, tinymce, weasyprint, appypod, sessions.
9 models:
=========================== ============================ ========= =======
 Name                        Default table                #fields   #rows
--------------------------- ---------------------------- --------- -------
 lets.Demand                 lets.Demands                 3         3
 lets.Offer                  lets.Offers                  4         5
 lets.Place                  lets.Places                  4         4
 lets.Product                lets.Products                4         6
 sessions.Session            sessions.SessionTable        3         ...
 system.SiteConfig           system.SiteConfigs           3         0
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates   5         2
 users.Authority             users.Authorities            3         0
 users.User                  users.AllUsers               17        11
=========================== ============================ ========= =======
<BLANKLINE>
