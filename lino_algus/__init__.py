# -*- coding: UTF-8 -*-
# Copyright 2016-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""This is the main module of Lino Algus.

.. autosummary::
   :toctree:

   lib
   projects


"""

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO.get('version')

intersphinx_urls = dict(docs="http://algus.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/algus/blob/master/%s'
doc_trees = ['docs']
