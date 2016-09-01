# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)

"""This is the main module of Lino Algus.

.. autosummary::
   :toctree:

   lib
   projects


"""

import os

filename = os.path.join(os.path.dirname(__file__), 'setup_info.py')
exec(compile(open(filename, "rb").read(), filename, 'exec'))

__version__ = SETUP_INFO.get('version')

intersphinx_urls = dict(docs="http://algus.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/algus/blob/master/%s'

