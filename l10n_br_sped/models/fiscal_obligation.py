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


from openerp.osv import osv, fields
from sped_contabil import generate_sped_contabil
from sped_fiscal import generate_sped_fiscal


class fiscal_obligation(osv.Model):
    _name = 'fiscal.obligation'
    _description = 'Geracao das obrigacoes fiscais'
    _order = 'description asc'
    _rec_name = 'description'
    _columns = {
        'code': fields.integer('Código'),
        'description': fields.char('Descrição', size=60),
        'generate': fields.boolean('Gerar obrigação'),
        'executions': fields.one2many('fiscal.obligation.execution', 'fiscal_obligation_id', 'Execuções'),
    }
    _defaults = {'generate': False,
                 'code': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'fiscal.obligation.messages.order.sequence'),
                 }

    def generate_obligation(self, cr, uid, ids=None, context=None):
        ids = self.search(cr, uid, [('generate', '=', True), ])
        obligations = self.browse(cr, uid, ids, context)
        for obligation in obligations:
            if obligation.description == 'Sped Fiscal':
                generator = generate_sped_fiscal()
                generator.generate(cr, uid, obligation.id, context, obligation)

            elif obligation.description == 'Sped Contabil':
                generator = generate_sped_contabil()
                generator.generate(cr, uid, obligation.id, context, obligation)

        return True


fiscal_obligation()


class fiscal_obligation_execution(osv.Model):
    _name = 'fiscal.obligation.execution'
    _description = 'Execucao da geracao da obrigacao fiscal'
    _order = 'code asc'
    _columns = {
        'code': fields.integer('Código'),
        'date_execution_start': fields.datetime('Inicio execução'),
        'date_execution_end': fields.datetime('Fim execução'),
        'running': fields.boolean('Executando'),
        'fiscal_obligation_id': fields.many2one('fiscal.obligation', 'Obrigação fiscal',
                                                required=True),
        'efd_fiscal_file': fields.binary('Arquivo EFD-Fiscal gerado',
                                         help="Arquivo resultante do processo de geração do EFD Fiscal"),
        'messages': fields.one2many('fiscal.obligation.messages',
                                    'fiscal_obligation_execution_id', 'Mensagens'),
    }
    _defaults = {
    }


class fiscal_obligation_messages(osv.Model):
    _name = 'fiscal.obligation.messages'
    _description = 'Mensagens ocorridas na geracao da obrigacao'
    _order = 'id asc'
    _columns = {
        'message': fields.char('Mensagem', size=500),
        'fiscal_obligation_execution_id': fields.many2one('fiscal.obligation.execution', 'Execução obrigação fiscal',
                                                          required=True),
    }
    _defaults = {}

fiscal_obligation_messages()


class contador(osv.Model):
    _description = 'Contadores da empresa'
    _inherit = 'res.partner'
    _columns = {
        'is_accountant': fields.boolean('Contador', help="Marque esta caixa se este parceiro é um contador."),
        'cnpj_empresa': fields.char('CNPJ escritório', size=20),
        'inscricao_crc': fields.char('Incrição CRC', size=15),
    }
    _defaults = {}

    def create(self, cr, uid, vals, context=None):
        if not context:
            context = {}
        vals.update({'is_accountant': True, 'customer': False})
        return super(contador, self).create(cr, uid, vals, context)


contador()


class account_asset(osv.Model):
    _description = 'Patrimonio imobilizado'
    _inherit = 'account.asset.asset'
    _columns = {
        # TODO Colocar aqui também a conta analitica de contabilização do item
        'tipo_mercadoria': fields.integer('Tipo mercadoria'),
    }
    _defaults = {}

account_asset()
