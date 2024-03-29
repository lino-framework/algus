# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)


"""Defines the standard user roles for Lino Algus."""


from lino.core.roles import UserRole, SiteAdmin, SiteUser, SiteStaff
from lino.modlib.users.choicelists import UserTypes
from django.utils.translation import gettext_lazy as _

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"),        UserRole, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("User"),             SiteUser,  'user')
add('500', _("Staff"),            SiteStaff, 'staff')
add('900', _("Administrator"),    SiteAdmin, 'admin')
