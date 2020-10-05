# -*- coding: UTF-8 -*-
# Copyright 2016-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""

.. autosummary::
   :toctree:

   doctests
   demo
   memory
   fixtures



"""

from lino_algus.lib.algus.settings import *


# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
TIME_ZONE = 'UTC'
