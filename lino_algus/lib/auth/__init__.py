# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)


"""
Lino Algus extension of :mod:`lino.modlib.auth`.

.. autosummary::
   :toctree:

    models
    desktop
    fixtures.demo
    fixtures.demo2

"""

from lino.modlib.auth import Plugin


class Plugin(Plugin):
   
    extends_models = ['User']

