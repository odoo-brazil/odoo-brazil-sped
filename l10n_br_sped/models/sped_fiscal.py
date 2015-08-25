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


from datetime import datetime
import base64


class generate_sped_fiscal():

    def __init__(self):
        self.execution_id = 0

    def _create_new_execution(
            self, cr, uid, ids=None, context=None, obligation=None):
        pool_execution = obligation.pool.get('fiscal.obligation.execution')
        new_obj = {'code': 1, 'date_execution_start': datetime.now(),
                   'date_execution_end': datetime.now(), 'running': True,
                   'fiscal_obligation_id': obligation.id}
        generated_id = pool_execution.create(cr, uid, new_obj, context)
        self.execution_id = generated_id
        return generated_id

    def _set_as_generated(
            self, cr, uid, ids=None, context=None, obligation=None, content=None):
        pool_obligation = obligation.pool.get('fiscal.obligation')
        pool_execution = obligation.pool.get('fiscal.obligation.execution')
        pool_obligation.write(cr, uid, ids, {'generate': False, }, context)

        print type(content)
        if not content is None:
            print content.encode('utf-8')
            result = base64.b64encode(content.encode('utf-8'))
            pool_execution.write(cr, uid, self.execution_id,
                                 {'date_execution_end': datetime.now(),
                                  'running': False,
                                  'efd_fiscal_file': result}, context)
        else:
            pool_execution.write(
                cr, uid, self.execution_id, {
                    'date_execution_end': datetime.now(), 'running': False}, context)

    def _create_new_message(self, cr, uid, ids=None, context=None, obligation=None,
                            execution_id=None, message=None):
        pool_message = obligation.pool.get('fiscal.obligation.messages')
        pool_message.create(
            cr, uid, {'message': message,
                      'fiscal_obligation_execution_id': execution_id}, context)

    def generate(self, cr, uid, ids=None, context=None, obligation=None):
        execution_id = self._create_new_execution(
            cr, uid, ids, context, obligation)
        self._create_new_message(cr, uid, ids, context, obligation,
                                 execution_id, "Iniciado a gerar o Sped Fiscal")

        companies = obligation.pool.get('res.company')
        company_ids = companies.search(cr, uid, [],
                                       offset=0, limit=1, context=context)
        if len(company_ids) > 0:
            company = companies.browse(cr, uid, company_ids[0], context)

            efd = None  # pysped_efd.EFD(
#                 COD_FIN='0',
#                 # adicionar estes atributos ao objeto fiscal_obligation
#                 DT_INI='01042013',
#                 DT_FIN='30042013',
#                 NOME=company.partner_id.legal_name,
#                 CNPJ=company.partner_id.cnpj_cpf,
#                 CPF='',
#                 UF=company.partner_id.l10n_br_city_id.state_id.code,
#                 IE=company.partner_id.inscr_est,
#                 COD_MUN=company.partner_id.l10n_br_city_id.ibge_code,
#                 IM=company.partner_id.inscr_mun,
#                 SUFRAMA=company.partner_id.suframa,
#                 IND_PERFIL='',
#                 # TODO Adicionar estes dois campos ao objeto company
#                 IND_ATIV=''
#             )

            self.bloco_0(cr, uid, ids, context, obligation, efd, company)
            self.bloco_C(cr, uid, ids, context, obligation, efd)
            self.bloco_D(cr, uid, ids, context, obligation, efd)
            self.bloco_E(cr, uid, ids, context, obligation, efd)
            self.bloco_G(cr, uid, ids, context, obligation, efd)
            self.bloco_H(cr, uid, ids, context, obligation, efd)
            self.bloco_1(cr, uid, ids, context, obligation, efd)
            self.bloco_9(cr, uid, ids, context, obligation, efd)
            content = efd.generate()

            self._set_as_generated(cr, uid, ids, context, obligation, content)
            self._create_new_message(
                cr, uid, ids, context, obligation, execution_id,
                "Terminado de gerar o Sped Fiscal")
        else:
            self._set_as_generated(cr, uid, ids, context, obligation)
            self._create_new_message(
                cr, uid, ids, context, obligation, execution_id,
                "Não foi possível encontrar a empresa padrão.")

    def bloco_0(self, cr, uid, ids, context, obligation,
                efd=None, company=None):
        pass
        # Abertura do Arquivo Digital e Identificação da entidade 0000 0 1
        # Abertura do Bloco 0 0001 1 1
        # Dados Complementares da entidade 0005 2 1
        # Dados do Contribuinte Substituto 0015 2 V
        # Dados do Contabilista 0100 2 1
        # Tabela de Cadastro do Participante 0150 2 V
        # Alteração da Tabela de Cadastro de Participante 0175 3 1:N
        # Identificação das unidades de medida 0190 2 V
        # Tabela de Identificação do Item (Produtos e Serviços) 0200 2 V
        # Alteração do Item 0205 3 1:N
        # Código de produto conforme Tabela ANP (Combustíveis) 0206 3 1:1
        # Fatores de Conversão de Unidades 0220 3 1:N
        # Cadastro de bens ou componentes do Ativo Imobilizado 0300 2 V
        # Informação sobre a Utilização do Bem 0305 3 1:1
        # Tabela de Natureza da Operação / Prestação 0400 2 V
        # Tabela de Informação Complementar do documento fiscal 0450 2 V
        # Tabela de Observações do Lançamento Fiscal 0460 2 V
        # Plano de contas contábeis 0500 2 V
        # Centro de custos 0600 2 V
        # Encerramento do Bloco 0 0990

        # -------------- REG 0001 ---------------
#         reg0001 = pysped_efd.r0001(IND_MOV='0')
#         efd.add(reg0001)
#
#         #--------------- REG 0005 ---------------
#         reg0005 = pysped_efd.r0005(FANTASIA=company.name, CEP=company.partner_id.zip,
#                                    END=company.partner_id.street, NUM=company.partner_id.number, COMPL=company.partner_id.street2,
#                                    BAIRRO=company.partner_id.district, FONE=company.partner_id.phone, FAX=company.partner_id.fax,
#                                    EMAIL=company.partner_id.email,)
#
#         efd.add(reg0005)

        #---------------- REG 0015 --------------
        # TODO Precisa de um cadastro de incrição estadual substituto reg0015

        #--------------- REG 0100 ---------------
#         partner_pool = obligation.pool.get('res.partner')
#         accountant_ids = partner_pool.search(
#             cr, uid, [('company_id', '=', company.id), ('is_accountant', '=', True)], context=context)
#         if len(accountant_ids) > 0:
#             accountant = partner_pool.browse(
#                 cr,
#                 uid,
#                 accountant_ids[0],
#                 context)
#
#             reg0100 = pysped_efd.r0100(NOME=accountant.name, CPF=accountant.cnpj_cpf,
#                                        CRC=accountant.inscricao_crc, CNPJ=accountant.cnpj_empresa,
#                                        CEP=accountant.zip, END=accountant.street, NUM=accountant.number,
#                                        COMPL=accountant.street2, BAIRRO=accountant.district, FONE=accountant.phone,
#                                        FAX=accountant.fax, EMAIL=accountant.email, COD_MUN=accountant.l10n_br_city_id.ibge_code)
#
#             efd.add(reg0100)
#         else:
#             self._create_new_message(
#                 cr,
#                 uid,
#                 ids,
#                 context,
#                 obligation,
#                 self.execution_id,
#                 "Informações sobre o contador não configuradas.")

        #--------------- REG 0150 ---------------
        # TODO Talvez em vez de pesquisar antes todos os clientes,
        # conforme for gerando os registros de entrada e saida, ir adicionando
        # os clientes automaticamente, ja que o componente ordena os registros.
#         customer_pool = obligation.pool.get('res.partner')
#         customer_ids = customer_pool.search(
#             cr, uid, [
#                 ('customer', '=', True)], context=context)
#         customers = customer_pool.browse(cr, uid, customer_ids, context)
#         for customer in customers:
#             reg0150 = pysped_efd.r0150(COD_PART=customer.id, NOME=customer.name, COD_PAIS=customer.country_id.bc_code,
#                                        CNPJ=customer.cnpj_cpf, CPF=customer.cnpj_cpf, IE=customer.inscr_est,
#                                        COD_MUN=customer.l10n_br_city_id.ibge_code, SUFRAMA=customer.suframa,
#                                        END=customer.street, NUM=customer.number, COMPL=customer.street2, BAIRRO=customer.district)
#
#             efd.add(reg0150)

        #--------------- REG 0175 ---------------
        # TODO Usar o audittrail.log para buscar as modificações.

        #--------------- REG 0190 ---------------
#         uom_pool = obligation.pool.get('product.uom')
#         ids = uom_pool.search(cr, uid, [], context=context)
#         units = uom_pool.browse(cr, uid, ids, context=context)
#         for unit in units:
#             reg0190 = pysped_efd.r0190(UNID=unit.id, DESCR=unit.name)
#             efd.add(reg0190)

        #--------------- REG 0200 ---------------
#         product_pool = obligation.pool.get('product.product')
#         ids = product_pool.search(cr, uid, [], context=context)
#         products = product_pool.browse(cr, uid, ids, context=context)
        # TODO TIPO_ITEM, ou criar um enumerador no cadastro, ou inferir o tipo dependendo de onde for usado
        # TODO NCM seria a classificação fiscal, porém não entendi como é o relacionamento
        # TODO Quando for serviço ainda falta o Tipo de serviço no cadastro
        # TODO Como pegar a aliquota default de icms para o item?
#         for product in products:
#             reg0200 = pysped_efd.r0200(COD_ITEM=product.default_code, DESCR_ITEM=product.name_template,
#                                        COD_BARRA=product.ean13, COD_ANT_ITEM='', UNID_INV=product.product_tmpl_id.uom_id.id,
#                                        TIPO_ITEM='0', COD_NCM='', EX_IPI='', COD_GEN='?',
#                                        COD_LST='', ALIQ_ICMS='?')
#             efd.add(reg0200)

        #--------------- REG 0205 ---------------
        # TODO Usar o audittrail.log para buscar as modificações.

        #--------------- REG 0206 ---------------
        # Registro correspondente aos combustiveis. Talvez seria necessário
        # outro módulo

        #--------------- REG 0220 ---------------
        # Registro de conversão de unidade de medida. Acho que não se aplica

        #--------------- REG 0300 ---------------
#         asset_pool = obligation.pool.get('account.asset.asset')
#         asset_ids = asset_pool.search(cr, uid, [], context=context)
#         assets = asset_pool.browse(cr, uid, asset_ids, context=context)
#         for asset in assets:
#             reg0300 = pysped_efd.r0300(COD_IND_BEM=asset.code, IDENT_MERC=asset.tipo_mercadoria,
#                                        DESCR_ITEM=asset.name, COD_PRNC=asset.parent_id.id,
#                                        COD_CTA=asset.category_id.id, NR_PARC=asset.method_number)
#             efd.add(reg0300)

        #--------------- REG 0305 ---------------
        # TODO modificar o asset para quando for tipo 1, acrescentar os campos
        # desse registro no cadastro

        #--------------- REG 0400 ---------------
        # TODO Usar categoria fiscal ou posição fiscal? Natureza da operação

        #--------------- REG 0450 ---------------
        # Necessita cadastro de informações adicionais, que posteriormente deve ser vinculado as faturas
        # e aparecer na nota de saida e entrada.

        #--------------- REG 0460 ---------------
        # mesmo caso do registro anterior.

        #--------------- REG 0500 ---------------
#         account_pool = obligation.pool.get('account.account')
#         account_ids = account_pool.search(
#             cr, uid, [
#                 ('company_id', '=', company.id)], context=context)
#         accounts = account_pool.browse(cr, uid, account_ids, context=context)
#         # TODO Falta a natureza e o tipo da conta.
#         for account in accounts:
#             reg0500 = pysped_efd.r0500(DT_ALT='', COD_NAT_CC='',
#                                        IND_CTA='', NIVEL=account.level, COD_CTA=account.code,
#                                        NOME_CTA=account.name)
#             efd.add(reg0500)
#
#         #--------------- REG 0600 ---------------
#         account_analytic_pool = obligation.pool.get('account.analytic.account')
#         analytic_ids = account_analytic_pool.search(
#             cr, uid, [
#                 ('company_id', '=', company.id)], context=context)
#         analytic_accounts = account_analytic_pool.browse(
#             cr,
#             uid,
#             analytic_ids,
#             context=context)
#         for analytic in analytic_accounts:
#             reg0600 = pysped_efd.r0600(
#                 DT_ALT='',
#                 COD_CCUS=analytic.code,
#                 CCUS=analytic.name)
#             efd.add(reg0600)

        #--------------- REG 0990 ---------------

    def bloco_C(self, cr, uid, ids, context, obligation, efd=None):
        pass
        # Abertura do Bloco C C001 1 1
        # Documento - Nota Fisca l (código 01) , Nota Fisca l Avulsa (código 1B) , Nota Fisca l de Produtor (código 04) e Nota Fisca l Eletrônica (código 55) C100 2 V
        # Operações com ICMS ST recolhido para UF diversa do destinatário do documento fisca l(Código 55) C105 3 1:1
        # Complemento de Documento - Informação Complementar da Nota Fisca l (código 01 ,1B , 55) C110 3 1:N
        # Complemento de Documento - Processo referenciado C111 4 1:N
        # Complemento de Documento - Documento de Arrecadação Referenciado C112 4 1:N
        # Complemento de Documento - Documento Fisca l Referenciado C113 4 1:N
        # Complemento de Documento - Cupom Fiscal Referenciado C114 4 1:N
        # Local de coleta e/ou entrega (CÓDIGOS 01 , 1B e 04) C115 4 1:N
        # Cupom Fiscal Eletrônico - CF-e referenciado C116 4 1:N
        # Complemento de Documento - Operações de Importação (código 01) C120 3 1:N
        # Complemento de Documento - ISSQN , IRRF e Previdência Social C130 3 1:1
        # Complemento de Documento - Fatura (código 01) C140 3 1:1
        # Complemento de Documento - Vencimento da Fatura (código 01) C141 4 1:N
        # Complemento de Documento - Volumes Transportados (código 01 e 04) Exceto Combustíveis C160 3 1:1
        # Complemento de Documento - Operações com combustíveis (código 01) C165 3 1:N
        # Complemento de Documento - Itens do Documento (código 01 , 1B , 04 e 55) C170 3 1:N
        # Complemento de Item - Armazenamento de Combustíveis (código 01,55) C171 4 1:N
        # Complemento de Item - Operações com ISSQN (código 01) C172 4 1:1
        # Complemento de Item - Operações com Medicamentos (código 01,55) C173 4 1:N
        # Complemento de Item - Operações com Armas de Fogo (código 01) C174 4 1:N
        # Complemento de Item - Operações com Veículos Novos (código 01,55) C175 4 1:N
        # Complemento de Item -Ressarcimento de ICMS em operações com Substituição Tributária (código 01,55) C176 4 1:N
        # Complemento de Item - Operações com Produtos Sujeitos a Selo de Controle IPI(código 01) C177 4 1:1
        # Complemento de Item - Operações com Produtos Sujeitos a Tributação de IP I por Unidade ou Quantidade de produto C178 4 1:1
        # Complemento de Item - Informações Complementares ST (código 01) C179 4 1:1
        # Registro Analítico do Documento (código 01 , 1B , 04 e 55) C190 3 1:N
        # Complemento do Registro Analítico - Observações do Lançamento Fisca l (código 01 ,1B e 55) C195 3 1:N
        # Outras Obrigações Tributárias , Ajustes e Informações provenientes de Documento Fiscal C197 4 1:N
        # Documento - Resumo Diário das Notas Fiscais de Venda a Consumidor (código 02) C300 2 V
        # Documentos Cancelados de Nota Fisca l de Venda a Consumidor (código 02) C310 3 1:N
        # Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02) C320 3 1:N
        # Itens dos Resumos Diários dos Documentos (código 02) C321 4 1:N
        # Nota Fisca l de venda a consumidor (código 02) C350 2 V
        # Itens do documento (código 02) C370 3 1:N
        # Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02) C390 3 1:N
        # Equipamento ECF (código 02 e 2D) C400 2 1:N
        # Redução Z (código 02 e 2D) C405 3 1:N
        # PIS e COFINS Totalizados no Dia (código 02 e 2D) C410 4 1:1
        # Registro dos Totalizadores Parciais da Redução Z (código 02 e 2D) C420 4 1:N
        # Resumo de itens do movimento diário (código 02 e 2D) C425 5 1:N
        # Documento Fiscal Emitido por ECF (código 02 e 2D) C460 4 1:N
        # Itens do Documento Fisca l Emitido por ECF (código 02 e 2D) C470 5 1:N
        # Registro Analítico do movimento diário (código 02 e 2D) C490 4 1:N
        # Resumo Mensa l de Itens do ECF por Estabelecimento (código 02 e 2D e 2E) C495 2 V
        # Nota Fiscal/Conta de Energia Elétrica (código 06) , Nota Fiscal/Conta de fornecimento
        # dágua canalizada (código 29) e Nota Fiscal/Consumo Fornecimento de Gás (Código 28) C500 2 V
        # Itens do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06) , Nota
        # Fiscal/Conta de fornecimento dágua canalizada (código 29) e Nota Fiscal/Conta
        # Fornecimento de Gás (Código 28) C510 3 1:N
        # Registro Analítico do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06) ,
        # Nota Fiscal/Conta de fornecimento dágua canalizada (código 29) e Nota Fiscal/Conta
        # Fornecimento de Gás (Código 28) C590 3 1:N
        # Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06) , Nota
        # Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento
        # de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03) C600 2 V
        # Documentos cancelados - Consolidação diária de notas fiscais/conta de energia elétrica
        #(Código 06) , nota fiscal/conta de fornecimento de água (código 29) e nota fiscal/conta
        # de fornecimento de gás (código 28) C601 3 1:N
        # Itens do Documento Consolidado - Notas Fiscais/Contas de Energia Elétrica (Código
        # 06) , Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de
        # Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03) C610 3 1:N
        # Registro Analítico dos Documentos - Notas Fiscais/Contas de Energia Elétrica (Código
        # 06) , Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de
        # Fornecimento de Gás (Código 28) C690 3 1:N
        # Consolidação dos Documentos Nota Fiscal/Conta Energia Elétrica (código 06) emitidas
        # em via única - (Empresas obrigadas à entrega do arquivo previsto no Convênio ICMS
        # 115/03) e Nota Fiscal/Conta de Fornecimento de Gás Canalizado (Código 28) C700 2 V
        # Registro Analítico dos Documentos - Nota Fiscal/Conta Energia Elétrica (código 06)
        # emitidas em via única C790 3 1:N
        # Registro de Informações de ICMS ST por UF C791 4 1:N
        # Registro Cupom Fisca l Eletrônico - CF-e (Código 59) C800 2 V
        # Registro Analítico do CF-e (Código 59) C850 3 1:N
        # Identificação do equipamento SAT-CF-e (Código 59) C860 2 1:N
        # Resumo diário de CF-e (Código 59) por equipamento SAT-CF-e C890 3 1:N
        # Encerramento do Bloco C C990 1 1
        pass

    def bloco_D(self, cr, uid, ids, context, obligation, efd=None):
        # Abertura do Bloco D D001 1 1
        # Nota Fisca l de Serviço de Transporte (código 07) e Conhecimentos de Transporte
                # Rodoviário de Cargas (código 08) , Conhecimento de Transporte de Cargas Avulso
                #(Código 8B) , Aquaviário de Cargas (código 09) , Aéreo (código 10) , Ferroviário de
                # Cargas (código 11) e Multimoda l de Cargas (código 26) e Nota Fisca l de Transporte
                # Ferroviário de Cargas(código 27) e Conhecimento de Transporte Eletrônico - CT-e (código 57) . D100 2 V
        # Itens do documento - Nota Fisca l de Serviços de Transporte (código 07) D110 3 1:N
        # Complemento da Nota Fisca l de Serviços de Transporte (código 07) D120 4 1:N
        # Complemento do Conhecimento Rodoviário de Cargas (código 08) e Conhecimento de
                # Transporte de Cargas Avulso (Código 8B) D130 3 1:N
        # Complemento do Conhecimento Aquaviário de Cargas (código 09) D140 3 1:1
        # Complemento do Conhecimento Aéreo de Cargas (código 10) D150 3 1:1
        # Carga Transportada (CÓDIGO 08 , 8B , 09 , 10 , 11 , 26 E 27) D160 3 1:N
        # Loca l de Coleta e Entrega (códigos 08 , 8B , 09 , 10 , 11 e 26) D161 4 1:1
        # Identificação dos documentos fiscais (código 08,8B , 09,10,11,26 e 27) D162 4 1:N
        # Complemento do Conhecimento Multimoda l de Cargas (código 26) D170 3 1:1
        # Modais (código 26) D180 3 1:N
        # Registro Analítico dos Documentos (CÓDIGO 07 , 08 , 8B , 09 , 10 , 11 , 26 , 27 e 57) D190 3 1:N
        # Observações do lançamento (CÓDIGO 07 , 08 , 8B , 09 , 10 , 11 , 26 , 27 e 57) D195 3 1:N
        # Outras obrigações tributárias , ajustes e informações de valores
        # provenientes do documento fiscal .D197 4 1:N

        # Registro Analítico dos bilhetes consolidados de Passagem Rodoviário (código 13) , de
                # Passagem Aquaviário (código 14) , de Passagem e Nota de Bagagem (código 15) e de
                # Passagem Ferroviário (código 16) D300 2 V
        # Documentos cancelados dos Bilhetes de Passagem Rodoviário (código 13) , de
                # Passagem Aquaviário (código 14) , de Passagem e Nota de Bagagem (código 15) e de
                # Passagem Ferroviário (código 16) D301 3 1:N
        # Complemento dos Bilhetes (código 13 , código 14 , código 15 e código 16) D310 3 1:N
        # Equipamento ECF (Códigos 2E , 13 , 14 , 15 e 16) D350 2 1:N
        # Redução Z (Códigos 2E , 13 , 14 , 15 e 16) D355 3 1:N
        # PIS E COFINS totalizados no dia (Códigos 2E , 13 , 14 , 15 e 16) D360 4 1:1
        # Registro dos Totalizadores Parciais da Redução Z (Códigos 2E , 13 , 14 , 15 e 16) D365 4 1:N
        # Complemento dos documentos informados (Códigos 13 , 14 , 15 , 16 E 2E) D370 5 1:N
        # Registro analítico do movimento diário (Códigos 13 , 14 , 15 , 16 E 2E) D390 4 1:N
        # Resumo do Movimento Diário (código 18) D400 2 V
        # Documentos Informados (Códigos 13 , 14 , 15 e 16) D410 3 1:N
        # Documentos Cancelados dos Documentos Informados (Códigos 13 , 14 , 15 e 16) D411 4 1:N
        # Complemento dos Documentos Informados (Códigos 13 , 14 , 15 e 16) D420 3 1:N
        # Nota Fisca l de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22) D500 2 V
        # Itens do Documento - Nota Fisca l de Serviço de Comunicação (código 21) e Serviço de
                # Telecomunicação (código 22) D510 3 1:N
        # Termina l Faturado D530 3 1:N
        # Registro Analítico do Documento (códigos 21 e 22) D590 3 1:N
        # Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código
                # 21) e de Serviço de Telecomunicação (código 22) D600 2 V
        # Itens do Documento Consolidado (códigos 21 e 22) D610 3 1:N
        # Registro Analítico dos Documentos (códigos 21 e 22) D690 3 1:N
        # Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código
                # 21) e de Serviço de Telecomunicação (código 22) D695 2 V
        # Itens do Documento Consolidado (códigos 21 e 22) D610 3 1:N
        # Registro Analítico dos Documentos (códigos 21 e 22) D690 3 1:N
        # Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código
                # 21) e de Serviço de Telecomunicação (código 22) D695 2 V
        # Registro Analítico dos Documentos (códigos 21 e 22) D696 3 1:N
        # Registro de informações de outras UFs , relativamente aos serviços “ não-medidos ” de
                # televisão por assinatura via satélite D697 4 1:N
        # Encerramento do Bloco D D990 1 1

        pass

    def bloco_E(self, cr, uid, ids, context, obligation, efd=None):
        # Abertura do Bloco E E001 1 1
        # Período de Apuração do ICMS E100 2 V
        # Apuração do ICMS - Operações Próprias E110 3 1:1
        # Ajuste/Benefício/Incentivo da Apuração do ICMS E111 4 1:N
        # Informações Adicionais dos Ajustes da Apuração do ICMS E112 5 1:N
        # Informações Adicionais dos Ajustes da Apuração do ICMS - Identificação dos
                # documentos fiscais E113 5 1:N
        # Informações Adicionais da Apuração do ICMS - Valores Declaratórios E115 4 1:N
        # Obrigações do ICMS a Recolher - Obrigações Próprias E116 4 1:N
        # Período de Apuração do ICMS - Substituição Tributária E200 2 V
        # Apuração do ICMS - Substituição Tributária E210 3 1:1
        # Ajuste/Benefício/Incentivo da Apuração do ICMS - Substituição Tributária E220 4 1:N
        # Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária E230 5 1:N
        # Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária -
                # Identificação dos documentos fiscais E240 5 1:N
        # Obrigações do ICMS a Recolher - Substituição Tributária E250 4 1:N
        # Período de Apuração do IP I E500 2 V
        # Consolidação dos Valores de IP I E510 3 1:N
        # Apuração do IP I E520 3 1:1
        # Ajustes da Apuração do IP I E530 4 1:N
        # Encerramento do Bloco E E990 1 1
        pass
        #regE100 = pysped_efd.rE100(DT_INI='01-03-2012', DT_FIN='31-03-2012')
        #efd.add(regE100)

    def bloco_G(self, cr, uid, ids, context, obligation, efd=None):
        # Abertura do Bloco G G001 1 1
        # ICMS - Ativo Permanente - CIAP G110 2 V
        # Movimentação de Bem do Ativo Imobilizado G125 3 1:N
        # Outros créditos CIAP G126 4 1:N
        # Identificação do documento fisca l G130 4 1:N
        # Identificação do item do documento fisca l G140 5 1:N
        # Encerramento do Bloco G G990 1 1
        pass

    def bloco_H(self, cr, uid, ids, context, obligation, efd=None):
        # Abertura do Bloco H H001 1 1
        # Totais do Inventário H005 2 V
        # Inventário H010 3 1:N
        # Informação complementar do Inventário H020 4 1.N
        # Encerramento do Bloco H H990 1 1
        pass

    def bloco_1(self, cr, uid, ids, context, obligation, efd=None):
        # Abertura do Bloco 1 1001 1 1
        # Obrigatoriedade de registros do Bloco 1 1010 2 1
        # Registro de Informações sobre Exportação 1100 2 V
        # Documentos Fiscais de Exportação 1105 3 1:N
        # Operações de Exportação Indireta - Mercadorias de terceiros 1110 4 1:N
        # Controle de Créditos Fiscais - ICMS 1200 2 V
        # Utilização de Créditos Fiscais - ICMS 1210 3 1:N
        # Movimentação diária de combustíveis 1300 2 V
        # Movimentação diária de combustíveis por tanque 1310 3 1:N
        # Volume de vendas 1320 4 1:N
        # Bombas 1350 2 V
        # Lacres das bombas 1360 3 1:N
        # Bicos da bomba 1370 3 1:N
        # Controle de produção de Usina 1390 2 V
        # Produção diária da usina 1391 3 1:N
        # Informação sobre Valor Agregado 1400 2 V
        # Nota fiscal/Conta de energia elétrica (código 06) - Operações Interestaduais 1500 2 1:N
        # Itens do documento Nota fiscal/Conta de energia elétrica (código 06) 1510 3 1:N
        # Tota l das operações com cartão de crédito e/ou débito 1600 2 V
        # Documentos fiscais utilizados 1700 2 V
        # Documentos fiscais cancelados/inutilizados 1710 3 1:N
        # DCTA - Demonstrativo de crédito do ICMS sobre transporte aéreo 1800 2 1:1
        # Indicador de sub-apuração do ICMS 1900 2 V
        # Período da sub-apuração do ICMS 1910 3 1:N
        # Sub-apuração do ICMS 1920 4 1:1
        # Ajuste/benefício/incentivo da sub-apuração do ICMS 1921 5 1:N
        # Informações adicionais dos ajustes da sub-apuração do ICMS 1922 6 1:N
        # Informações adicionais dos ajustes da sub-apuração do ICMS - Identificação dos documentos fiscais 1923 6 1N
        # Informações adicionais da sub-apuração do ICMS - Valores declaratórios 1925 5 1:N
        # Obrigações do ICMS a recolher - Operações referentes à sub-apuração do ICMS 1926 5 1:N
        # Encerramento do Bloco 1 1990 1 1
        pass

    def bloco_9(self, cr, uid, ids, context, obligation, efd=None):
        # Abertura do Bloco 9 9001 1 1
        # Registros do Arquivo 9900 2 V
        # Encerramento do Bloco 9 9990 1 1
        # Encerramento do Arquivo Digita l 9999 0 1
        pass
