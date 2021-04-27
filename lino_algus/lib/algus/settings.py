# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.projects.std.settings import *
from lino_algus import SETUP_INFO

class Site(Site):

    verbose_name = "Lino Algus"
    description = SETUP_INFO['description']
    version = SETUP_INFO['version']
    url = SETUP_INFO['url']

    demo_fixtures = ['std', 'demo', 'demo2']
    user_types_module = 'lino_algus.lib.algus.user_types'
    migration_class = 'lino_algus.lib.algus.migrate.Migrator'

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps`.

        """
        yield super(Site, self).get_installed_apps()
        yield 'lino_algus.lib.users'
        yield 'lino_algus.lib.lets'
        yield 'lino_algus.lib.algus'
        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.tinymce'
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'


    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        tb.add_action('lets.Products')
