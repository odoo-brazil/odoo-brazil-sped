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

import re
from sped.ecd.registros import Registro0007, Registro0020
from ..sped_base import SpedBase
from datetime import date


class Bloco0(SpedBase):

    def generate(self, cr, uid, ids=None, context=None,
                 obligation=None, arquivo_digital=None):
        # Adicionar esse período na tela inicial
        start_date = date(2015, 1, 1)
        end_date = date(2015, 12, 31)

        company_pool = obligation.pool.get('res.company')
        company_id = 1  # TODO
        company = company_pool.browse(cr, uid, company_id, context)
        #
        # REGISTRO 0000: ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO
        #
        registro_abertura = arquivo_digital._registro_abertura
        registro_abertura.DT_INI = start_date
        registro_abertura.DT_FIN = end_date
        registro_abertura.NOME = company.partner_id.legal_name
        registro_abertura.CNPJ = re.sub('[^0-9]', '',
                                        company.partner_id.cnpj_cpf or '')
        registro_abertura.UF = company.partner_id.l10n_br_city_id.state_id.code
        registro_abertura.IE = re.sub('[^0-9a-zA-Z]', '',
                                      company.partner_id.inscr_est or '')
        registro_abertura.COD_MUN = \
            int((company.partner_id.state_id.ibge_code or '0') + 
                (company.partner_id.l10n_br_city_id.ibge_code or '0'))
        registro_abertura.IM = re.sub('[^0-9a-zA-Z]', '',
                                      company.partner_id.inscr_mun or '')

        #registro_abertura.IND_SIT_INI_PER = '3'
        #registro_abertura.IND_NIRE = '1'
        #registro_abertura.IND_FIN_ESC = '0'
        #registro_abertura.IND_GRANDE_PORTE = '0'
        #registro_abertura.TIP_ECD = '0'

        bloco_0 = arquivo_digital._blocos['0']

        #
        # REGISTRO 0007: OUTRAS INSCRIÇÕES CADASTRAIS DA PESSOA JURÍDICA
        #
        registro_0007 = Registro0007()
        registro_0007.COD_ENT_REF = '00'  # Sem registro
        bloco_0.add(registro_0007)

        #
        # REGISTRO 0020: ESCRITURAÇÃO CONTÁBIL DESCENTRALIZADA
        #
        childs = company_pool.search(cr, uid, [('parent_id', '=', company.id)])

        for child in company_pool.browse(cr, uid, childs, context):
            if child.expects_chart_of_accounts:
                registro_0020 = Registro0020()
                registro_0020.IND_DEC = '1'
                registro_0020.CNPJ = re.sub('[^0-9]', '',
                                            child.partner_id.cnpj_cpf or '')
                registro_0020.UF = \
                    child.partner_id.l10n_br_city_id.state_id.code
                registro_0020.IE = re.sub('[^0-9a-zA-Z]', '',
                                          child.partner_id.inscr_est or '')
                registro_0020.COD_MUN = \
                    (child.partner_id.state_id.ibge_code or '') +\
                    (child.partner_id.l10n_br_city_id.ibge_code or '')                    
                registro_0020.IM = re.sub('[^0-9a-zA-Z]', '',
                                          child.partner_id.inscr_mun or '')
                #registro_0020.NIRE = ''

                bloco_0.add(registro_0020)
