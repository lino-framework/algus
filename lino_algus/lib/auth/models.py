# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)

"""Database models for this plugin.

"""

from lino.api import dd, _

from lino.modlib.auth.models import *


class User(User):

    class Meta(User.Meta):
        app_label = 'auth'
        abstract = dd.is_abstract_model(__name__, 'User')

    place = models.ForeignKey('lets.Place', blank=True, null=True)


