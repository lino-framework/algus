# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from .demo import *
SITE = Site(globals())
DATABASES['default']['NAME'] = ':memory:'
