.. doctest docs/specs/roles.rst
.. _algus.specs.roles:

========================
User roles in Lino Algus
========================

>>> import lino
>>> lino.startup('lino_algus.projects.algus1.settings.doctests')
>>> from lino.api.doctest import *

Menus
-----

Site administrator
------------------

Rolf is a :term:`site administrator`, he has a complete menu.

>>> ses = rt.login('robin')
>>> ses.user.user_type
<users.UserTypes.admin:900>

>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Local Exchange : offers, demands
- Configure :
  - System : Users, Site Parameters
- Explorer :
  - System : Authorities, User types, User roles
- Site : About
