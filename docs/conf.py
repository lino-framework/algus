# -*- coding: utf-8 -*-
from lino.sphinxcontrib import configure
configure(globals(), 'lino_algus.projects.algus1.settings.doctests')

extensions += ['lino.sphinxcontrib.help_texts_extractor']
help_texts_builder_targets = {
    'lino_algus.': 'lino_algus.lib.algus'
}

project = "Lino Algus"
copyright = '2016-2021 Rumma & Ko Ltd'

html_title = "Lino Algus"
# html_context.update(public_url='https://algus.lino-framework.org')
