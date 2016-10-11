.. _algus.specs.roles:

========================
User roles in Lino Algus
========================

.. To run only this test::

    $ python setup.py test -s tests.SpecsTests.test_roles

    doctest init:

    >>> import lino
    >>> lino.startup('lino_algus.projects.algus.settings.doctests')
    >>> from lino.api.doctest import *

Menus
-----

System administrator
--------------------

Rolf is a system administrator, he has a complete menu.

>>> ses = rt.login('robin') 
>>> ses.user.profile
users.UserTypes.admin:900

>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Local Exchange : offers, demands
- Configure :
  - System : Site Parameters, Users
- Explorer :
  - System : Authorities, User types
- Site : About


