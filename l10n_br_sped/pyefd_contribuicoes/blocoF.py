# -*- coding: iso-8859-1 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Informática Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author: Daniel Hartmann <daniel@proge.com.br>                             #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                            #
##############################################################################

from Registro import RegistroX001, Registro
from RegistroX990 import RegistroX990
from util import Ocorrencia, Obrigatoriedade


class RegistroF001(RegistroX001):
    '''Abertura do bloco F'''

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "F001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.IND_MOV))
        return linha + super(RegistroF001, self).gerar_linha()


class RegistroF010(Registro):
    '''Identificação do estabelecimento'''

    def __init__(self):
        self.REG_PAI = "F001"
        self.REG = "F010"
        self.CNPJ = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.CNPJ))
        return linha + super(RegistroF010, self).gerar_linha()


class RegistroF100(Registro):
    '''Demais documentos e operações geradoras de contribuição e créditos.'''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F100"
        self.IND_OPER = ""
        self.COD_PART = ""
        self.COD_ITEM = ""
        self.DT_OPER = ""
        self.VL_OPER = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.NAT_BC_CRED = ""
        self.IND_ORIG_CRED = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_DOC_OPER = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.COD_PART,
            self.COD_ITEM,
            self.DT_OPER,
            self.VL_OPER,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.NAT_BC_CRED,
            self.IND_ORIG_CRED,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_DOC_OPER,
            ))
        return linha + super(RegistroF100, self).gerar_linha()


class RegistroF111(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "F100"
        self.REG = "F111"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF111, self).gerar_linha()


class RegistroF120(Registro):
    '''
    Bens incorporados ao ativo imobilizado - operações geradoras de créditos
    com base nos encargos de depreciação e amortização.
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F120"
        self.NAT_BC_CRED = ""
        self.IDENT_BEM_IMOB = ""
        self.IND_ORIG_CRED = ""
        self.IND_UTIL_BEM_IMOB = ""
        self.VL_OPER_DEP = ""
        self.PARC_OPER_NAO_BC_C_RED = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_BEM_IMOB = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.IDENT_BEM_IMOB,
            self.IND_ORIG_CRED,
            self.IND_UTIL_BEM_IMOB,
            self.VL_OPER_DEP,
            self.PARC_OPER_NAO_BC_C_RED,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_BEM_IMOB,
            ))
        return linha + super(RegistroF120, self).gerar_linha()


class RegistroF129(Registro):
    '''Processo referenciado.'''

    def __init__(self):
        self.REG_PAI = "F120"
        self.REG = "F129"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF129, self).gerar_linha()


class RegistroF130(Registro):
    '''
    Bens incorporados ao ativo imobilizado - operações geradoras de créditos
    com base no valor de aquisição/contribuição.
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F130"
        self.NAT_BC_CRED = ""
        self.IDENT_BEM_IMOB = ""
        self.IND_ORIG_CRED = ""
        self.IND_UTIL_BEM_IMOB = ""
        self.MES_OPER_AQUIS = ""
        self.VL_OPER_AQUIS = ""
        self.PARC_OPER_NAO_BC_CRED = ""
        self.VL_BC_CRED = ""
        self.IND_NR_PARC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_BEM_IMOB = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.IDENT_BEM_IMOB,
            self.IND_ORIG_CRED,
            self.IND_UTIL_BEM_IMOB,
            self.MES_OPER_AQUIS,
            self.VL_OPER_AQUIS,
            self.PARC_OPER_NAO_BC_CRED,
            self.VL_BC_CRED,
            self.IND_NR_PARC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_BEM_IMOB,
            ))
        return linha + super(RegistroF130, self).gerar_linha()


class RegistroF139(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "F130"
        self.REG = "F139"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF139, self).gerar_linha()


class RegistroF150(Registro):
    '''Crédito presumido sobre estoque de abertura'''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F150"
        self.NAT_BC_CRED = ""
        self.VL_TOT_EST = ""
        self.EST_IMP = ""
        self.VL_BC_EST = ""
        self.VL_BC_MEN_EST = ""
        self.CST_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_CRED_PIS = ""
        self.CST_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_CRED_COFINS = ""
        self.DESC_EST = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.VL_TOT_EST,
            self.EST_IMP,
            self.VL_BC_EST,
            self.VL_BC_MEN_EST,
            self.CST_PIS,
            self.ALIQ_PIS,
            self.VL_CRED_PIS,
            self.CST_COFINS,
            self.ALIQ_COFINS,
            self.VL_CRED_COFINS,
            self.DESC_EST,
            self.COD_CTA,
            ))
        return linha + super(RegistroF150, self).gerar_linha()


class RegistroF200(Registro):
    '''Operações da atividade imobiliária - Unidade imobiliária vendida'''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F200"
        self.IND_OPER = ""
        self.UNID_IMOB = ""
        self.IDENT_EMP = ""
        self.DESC_UNID_IMOB = ""
        self.NUM_CONT = ""
        self.CPF_CNPJ_ADQU = ""
        self.DT_OPER = ""
        self.VL_TOT_VEND = ""
        self.VL_REC_ACUM = ""
        self.VL_TOT_REC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.PERC_REC_RECEB = ""
        self.IND_NAT_EMP = ""
        self.INF_COMP = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.UNID_IMOB,
            self.IDENT_EMP,
            self.DESC_UNID_IMOB,
            self.NUM_CONT,
            self.CPF_CNPJ_ADQU,
            self.DT_OPER,
            self.VL_TOT_VEND,
            self.VL_REC_ACUM,
            self.VL_TOT_REC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.PERC_REC_RECEB,
            self.IND_NAT_EMP,
            self.INF_COMP,
            ))
        return linha + super(RegistroF200, self).gerar_linha()


class RegistroF205(Registro):
    '''
    Operações da atividade imobiliária - Custo incorrido da unidade imobiliária

    FIXME:
    Obs.: no layout, faltam os campos de no. 14 e 15. Como deve ficar
          o formato correto do arquivo ?
    '''

    def __init__(self):
        self.REG_PAI = "F200"
        self.REG = "F205"
        self.VL_CUS_INC_ACUM_ANT = ""
        self.VL_CUS_INC_PER_ESC = ""
        self.VL_CUS_INC_ACUM = ""
        self.VL_EXC_BC_CUS_INC_ACUM = ""
        self.VL_BC_CUS_INC = ""
        self.CST_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_CRED_PIS_ACUM = ""
        self.VL_CRED_PIS_DESC_ANT = ""
        self.VL_CRED_PIS_DESC = ""
        self.VL_CRED_PIS_DESC_FUT = ""
        self.CST_COFINS = ""
        # Falta o campo 14 ?
        # Falta o campo 15 ?
        self.ALIQ_COFINS = ""
        self.VL_CRED_COFINS_ACUM = ""
        self.VL_CRED_COFINS_DESC_ANT = ""
        self.VL_CRED_COFINS_DESC = ""
        self.VL_CRED_COFINS_DESC_FUT = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_CUS_INC_ACUM_ANT,
            self.VL_CUS_INC_PER_ESC,
            self.VL_CUS_INC_ACUM,
            self.VL_EXC_BC_CUS_INC_ACUM,
            self.VL_BC_CUS_INC,
            self.CST_PIS,
            self.ALIQ_PIS,
            self.VL_CRED_PIS_ACUM,
            self.VL_CRED_PIS_DESC_ANT,
            self.VL_CRED_PIS_DESC,
            self.VL_CRED_PIS_DESC_FUT,
            self.CST_COFINS,
            # Falta o campo 14 ?
            # Falta o campo 15 ?
            self.ALIQ_COFINS,
            self.VL_CRED_COFINS_ACUM,
            self.VL_CRED_COFINS_DESC_ANT,
            self.VL_CRED_COFINS_DESC,
            self.VL_CRED_COFINS_DESC_FUT,
            ))
        return linha + super(RegistroF205, self).gerar_linha()


class RegistroF210(Registro):
    '''
    Operações da atividade imobiliária - Custo orcado da unidade imobiliária
    vendida.

    FIXME:
    Obs.: no layout, faltam os campos de no. 1 a 3. Como deve ficar
          o formato correto do arquivo ?
    '''

    def __init__(self):
        self.REG_PAI = "F200"
        self.REG = "F210"
        self.VL_CUS_ORC = ""
        self.VL_EXC = ""
        self.VL_CUS_ORC_AJU = ""
        self.VL_BC_CRED = ""
        self.CST_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_CRED_PIS_UTIL = ""
        self.CST_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_CRED_COFINS_UTIL = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_CUS_ORC,
            self.VL_EXC,
            self.VL_CUS_ORC_AJU,
            self.VL_BC_CRED,
            self.CST_PIS,
            self.ALIQ_PIS,
            self.VL_CRED_PIS_UTIL,
            self.CST_COFINS,
            self.ALIQ_COFINS,
            self.VL_CRED_COFINS_UTIL,
            ))
        return linha + super(RegistroF210, self).gerar_linha()


class RegistroF211(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "F200"
        self.REG = "F211"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF211, self).gerar_linha()


class RegistroF500(Registro):
    '''
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de
    Tributação com Base no Lucro Presumido - Incidência do PIS/Pasep e da
    Cofins pelo Regime de Caixa
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F500"
        self.VL_REC_CAIXA = ''
        self.CST_PIS = ''
        self.VL_DESC_PIS = ''
        self.VL_BC_PIS = ''
        self.ALIQ_PIS = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.VL_DESC_COFINS = ''
        self.VL_BC_COFINS = ''
        self.ALIQ_COFINS = ''
        self.VL_COFINS = ''
        self.COD_MOD = ''
        self.CFOP = ''
        self.COD_CTA = ''
        self.INFO_COMPL = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se em 0110 COD_INC_TRIB = 2 e IND_REG_CUM = 1
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_REC_CAIXA,
            self.CST_PIS,
            self.VL_DESC_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_DESC_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_MOD,
            self.CFOP,
            self.COD_CTA,
            self.INFO_COMPL,
            ))
        return linha + super(RegistroF500, self).gerar_linha()


class RegistroF509(Registro):
    '''Processo Referenciado'''

    def __init__(self):
        self.REG_PAI = "F500"
        self.REG = "F509"
        self.NUM_PROC = ''
        self.IND_PROC = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF509, self).gerar_linha()


class RegistroF510(Registro):
    '''
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de
    Tributação com Base no Lucro Presumido - Incidência do PIS/Pasep e da
    Cofins pelo Regime de Caixa (Apuração da Contribuição por Unidade de Medida
    de Produto)
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F510"
        self.VL_REC_CAIXA = ''
        self.CST_PIS = ''
        self.VL_DESC_PIS = ''
        self.QUANT_BC_PIS = ''
        self.ALIQ_PIS_QUANT = ''
        self.VL_PIS = ''
        self.VL_PIS = ''
        self.VL_DESC_COFINS = ''
        self.QUANT_BC_COFINS = ''
        self.ALIQ_COFINS_QUANT = ''
        self.VL_COFINS = ''
        self.COD_MOD = ''
        self.CFOP = ''
        self.COD_CTA = ''
        self.INFO_COMPL = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se em 0110 COD_INC_TRIB = 2 e IND_REG_CUM = 1
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_REC_CAIXA,
            self.CST_PIS,
            self.VL_DESC_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.VL_PIS,
            self.VL_DESC_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_MOD,
            self.CFOP,
            self.COD_CTA,
            self.INFO_COMPL,
            ))
        return linha + super(RegistroF510, self).gerar_linha()


class RegistroF519(Registro):
    '''Processo Referenciado'''

    def __init__(self):
        self.REG_PAI = "F510"
        self.REG = "F519"
        self.NUM_PROC = ''
        self.IND_PROC = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF519, self).gerar_linha()


class RegistroF525(Registro):
    '''
    Composição da Receita Escriturada no Período - Detalhamento da Receita
    Recebida pelo Regime de Caixa
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F525"
        self.VL_REC = ''
        self.IND_REC = ''
        self.CNPJ_CPF = ''
        self.NUM_DOC = ''
        self.COD_ITEM = ''
        self.VL_REC_DET = ''
        self.CST_PIS = ''
        self.CST_COFINS = ''
        self.INFO_COMPL = ''
        self.COD_CTA = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_REC,
            self.IND_REC,
            self.CNPJ_CPF,
            self.NUM_DOC,
            self.COD_ITEM,
            self.VL_REC_DET,
            self.CST_PIS,
            self.CST_COFINS,
            self.INFO_COMPL,
            self.COD_CTA,
            ))
        return linha + super(RegistroF525, self).gerar_linha()


class RegistroF550(Registro):
    '''
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de
    Tributação com Base no Lucro Presumido - Incidência do PIS/Pasep e da
    Cofins pelo Regime de Competência
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F550"
        self.VL_REC_COMP = ''
        self.CST_PIS = ''
        self.VL_DESC_PIS = ''
        self.VL_BC_PIS = ''
        self.ALIQ_PIS = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.VL_DESC_COFINS = ''
        self.VL_BC_COFINS = ''
        self.ALIQ_COFINS = ''
        self.VL_COFINS = ''
        self.COD_MOD = ''
        self.CFOP = ''
        self.COD_CTA = ''
        self.INFO_COMPL = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se em 0110 COD_INC_TRIB = 2 e IND_REG_CUM = 2
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_REC_COMP,
            self.CST_PIS,
            self.VL_DESC_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_DESC_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_MOD,
            self.CFOP,
            self.COD_CTA,
            self.INFO_COMPL,
            ))
        return linha + super(RegistroF550, self).gerar_linha()


class RegistroF559(Registro):
    '''Processo Referenciado'''

    def __init__(self):
        self.REG_PAI = "F550"
        self.REG = "F559"
        self.NUM_PROC = ''
        self.IND_PROC = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF559, self).gerar_linha()


class RegistroF560(Registro):
    '''
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de
    Tributação com Base no Lucro Presumido - Incidência do PIS/Pasep e da
    Cofins pelo Regime de Competência (Apuração da Contribuição por Unidade de
    Medida de Produto)
    '''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F560"
        self.VL_REC_COMP = ''
        self.CST_PIS = ''
        self.VL_DESC_PIS = ''
        self.QUANT_BC_PIS = ''
        self.ALIQ_PIS_QUANT = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.VL_DESC_COFINS = ''
        self.QUANT_BC_COFINS = ''
        self.ALIQ_COFINS_QUANT = ''
        self.VL_COFINS = ''
        self.COD_MOD = ''
        self.CFOP = ''
        self.COD_CTA = ''
        self.INFO_COMPL = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se em 0110 COD_INC_TRIB = 2 e IND_REG_CUM = 2
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_REC_COMP,
            self.CST_PIS,
            self.VL_DESC_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_DESC_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_MOD,
            self.CFOP,
            self.COD_CTA,
            self.INFO_COMPL,
            ))
        return linha + super(RegistroF560, self).gerar_linha()


class RegistroF569(Registro):
    '''Processo Referenciado'''

    def __init__(self):
        self.REG_PAI = "F560"
        self.REG = "F569"
        self.NUM_PROC = ''
        self.IND_PROC = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroF569, self).gerar_linha()


class RegistroF600(Registro):
    '''Contribuição retida na fonte'''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F600"
        self.IND_NAT_RET = ""
        self.DT_REC_RET = ""
        self.VL_REC = ""
        self.VL_RET_FONT = ""
        self.COD_REC = ""
        self.IND_NAT_REC = ""
        self.CNPJ = ""
        self.VL_RET_PIS = ""
        self.VL_RET_COFINS = ""
        self.IND_DEC = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_RET,
            self.DT_REC_RET,
            self.VL_REC,
            self.VL_RET_FONT,
            self.COD_REC,
            self.IND_NAT_REC,
            self.CNPJ,
            self.VL_RET_PIS,
            self.VL_RET_COFINS,
            self.IND_DEC,
            ))
        return linha + super(RegistroF600, self).gerar_linha()


class RegistroF700(Registro):
    '''Deduções diversas'''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F700"
        self.IND_ORI_DED = ""
        self.IND_NAT_DED = ""
        self.VL_DED_PIS = ""
        self.VL_DED_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_ORI_DED,
            self.IND_NAT_DED,
            self.VL_DED_PIS,
            self.VL_DED_COFINS,
            ))
        return linha + super(RegistroF700, self).gerar_linha()


class RegistroF800(Registro):
    '''Identificação do estabelecimento'''

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F800"
        self.IND_NAT_EVEN = ""
        self.DT_EVEN = ""
        self.CNPJ_SUCED = ""
        self.PA_CONT_CRED = ""
        self.COD_CRED = ""
        self.VL_CRED = ""
        self.PER_CRED_CIS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_EVEN,
            self.DT_EVEN,
            self.CNPJ_SUCED,
            self.PA_CONT_CRED,
            self.COD_CRED,
            self.VL_CRED,
            self.PER_CRED_CIS,
            ))
        return linha + super(RegistroF800, self).gerar_linha()


class RegistroF990(RegistroX990):
    '''Encerramento do bloco F'''

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "F990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(RegistroF990, self).gerar_linha()
