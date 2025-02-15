##############################################################################
#
#       ______ Releasing children from poverty      _
#      / ____/___  ____ ___  ____  ____ ___________(_)___  ____
#     / /   / __ \/ __ `__ \/ __ \/ __ `/ ___/ ___/ / __ \/ __ \
#    / /___/ /_/ / / / / / / /_/ / /_/ (__  |__  ) / /_/ / / / /
#    \____/\____/_/ /_/ /_/ .___/\__,_/____/____/_/\____/_/ /_/
#                        /_/
#                            in Jesus' name
#
#    Copyright (C) 2023 Compassion CH (http://www.compassion.ch)
#    @author: Emanuel Cino, Simon Gonzalez <sgonzalez@ikmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# pylint: disable=C8101
{
    "name": "Periodic Accounting Transfer",
    "summary": "Move from an ending accounting period to an open one",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Compassion CH",
    "development_status": "Production/Stable",
    "website": "https://github.com/CompassionCH/test-repo",
    "category": "Accounting",
    "depends": [
        "account",  # source/addons/account
        "account_lock_date_update",  # oca_addons/account-financial-tools
    ],
    "external_dependencies": {},
    "data": ["views/account_update_lock_date.xml"],
    "installable": True,
}
