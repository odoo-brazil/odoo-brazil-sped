# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 TrustCode - www.trustcode.com.br                         #
#              Danimar Ribeiro <danimaribeiro@gmail.com>                      #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################


{
    "name": "Sped Fiscal Brasil",
    "version": "1.0",
    "depends": ["base"],
    "author": "KMEE, TrustCode",
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'website': 'https://github.com/odoo-brazil/',
    "description": """
      Este módulo permite a geração das obrigações fiscais da
      localização brasileira.
    """,
    'contributors': ['Danimar Ribeiro <danimaribeiro@gmail.com>',
                     ],
    'depends': [
        'l10n_br_base',
        'account_asset',
    ],
    'data': ['views/l10n_br_fiscal_obligation.xml'],
    'installable': True,
}
