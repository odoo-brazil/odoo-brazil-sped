# -*- coding: iso-8859-1 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Informática Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author Daniel Hartmann <daniel@proge.com.br>                              #
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

from Registro import RegistroX001
from RegistroX990 import RegistroX990
from bloco9 import Registro
from util import Ocorrencia, Obrigatoriedade


class RegistroD001(RegistroX001):
    '''Abertura do bloco D'''

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "D001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.IND_MOV))
        return linha + super(RegistroD001, self).gerar_linha()


class RegistroD010(Registro):
    '''Identificação do estabelecimento'''

    def __init__(self):
        self.REG_PAI = "D001"
        self.REG = "D010"
        self.CNPJ = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.CNPJ))
        return linha + super(RegistroD010, self).gerar_linha()


class RegistroD100(Registro):
    '''
    Aquisição de Serviços de Transportes (Códigos 07, 08, 8B, 09, 10, 11, 26,
    27 e 57)
    '''

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D100"
        self.IND_OPER = ""
        self.IND_EMIT = ""
        self.COD_PART = ""
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.CHV_CTE = ""
        self.DT_DOC = ""
        self.DT_A_P = ""
        self.TP_CTE = ""
        self.CHV_CTE_REF = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.IND_FRT = ""
        self.VL_SERV = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.VL_NT = ""
        self.COD_INF = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.IND_EMIT,
            self.COD_PART,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.CHV_CTE,
            self.DT_DOC,
            self.DT_A_P,
            self.TP_CTE,
            self.CHV_CTE_REF,
            self.VL_DOC,
            self.VL_DESC,
            self.IND_FRT,
            self.VL_SERV,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_NT,
            self.COD_INF,
            self.COD_CTA,
            ))
        return linha + super(RegistroD100, self).gerar_linha()


class RegistroD101(Registro):
    '''
    Complemento do documento de transporte (Códigos 07, 08, 8B, 09, 10, 11, 26,
    27 e 57) - PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "D100"
        self.REG = "D101"
        self.IND_NAT_FRT = ""
        self.VL_ITEM = ""
        self.CST_PIS = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_FRT,
            self.VL_ITEM,
            self.CST_PIS,
            self.NAT_BC_CRED,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD101, self).gerar_linha()


class RegistroD105(Registro):
    '''
    Complemento do documento de transporte (códigos 07, 08, 8B, 09, 10, 11, 26,
    27 e 57) - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "D100"
        self.REG = "D105"
        self.IND_NAT_FRT = ""
        self.VL_ITEM = ""
        self.CST_COFINS = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_FRT,
            self.VL_ITEM,
            self.CST_COFINS,
            self.NAT_BC_CRED,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD105, self).gerar_linha()


class RegistroD111(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "D100"
        self.REG = "D111"
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
        return linha + super(RegistroD111, self).gerar_linha()


class RegistroD200(Registro):
    '''
    Resumo da Escrituração Diária - Prestação de Serviços de Transportes
    (Códigos 07, 08, 8B, 09, 10, 11, 26, 27 e 57)
    '''

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D200"
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.NUM_DOC_INI = ""
        self.NUM_DOC_FIN = ""
        self.CFOP = ""
        self.DT_REF = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.NUM_DOC_INI,
            self.NUM_DOC_FIN,
            self.CFOP,
            self.DT_REF,
            self.VL_DOC,
            self.VL_DESC,
            ))
        return linha + super(RegistroD200, self).gerar_linha()


class RegistroD201(Registro):
    '''Totalização do resumo diário - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "D200"
        self.REG = "D201"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.VL_ITEM,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD201, self).gerar_linha()


class RegistroD205(Registro):
    '''Totalização do resumo diário - Cofins'''

    def __init__(self):
        self.REG_PAI = "D200"
        self.REG = "D205"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.VL_ITEM,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD205, self).gerar_linha()


class RegistroD209(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "D200"
        self.REG = "D209"
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
        return linha + super(RegistroD209, self).gerar_linha()


class RegistroD300(Registro):
    '''
    Resumo da escrituração diária - Bilhetes consolidados de passagem
    rodoviário (código 13), de passagem aquaviário (código 14), de passagem e
    nota de bagagem (código 15) e de passagem ferroviário (código 16)
    '''

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D300"
        self.COD_MOD = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC_INI = ""
        self.NUM_DOC_FIN = ""
        self.CFOP = ""
        self.DT_REF = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.SER,
            self.SUB,
            self.NUM_DOC_INI,
            self.NUM_DOC_FIN,
            self.CFOP,
            self.DT_REF,
            self.VL_DOC,
            self.VL_DESC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD300, self).gerar_linha()


class RegistroD309(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "D300"
        self.REG = "D309"
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
        return linha + super(RegistroD309, self).gerar_linha()


class RegistroD350(Registro):
    '''
    Resumo diário de cupom fiscal emitido por ECF - (códigos 2E, 13, 14, 15 e
    16)
    '''

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D350"
        self.COD_MOD = ""
        self.ECF_MOD = ""
        self.ECF_FAB = ""
        self.DT_DOC = ""
        self.CRO = ""
        self.CRZ = ""
        self.NUM_COO_FIN = ""
        self.GT_FIN = ""
        self.VL_BRT = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.ECF_MOD,
            self.ECF_FAB,
            self.DT_DOC,
            self.CRO,
            self.CRZ,
            self.NUM_COO_FIN,
            self.GT_FIN,
            self.VL_BRT,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD350, self).gerar_linha()


class RegistroD359(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "D350"
        self.REG = "D359"
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
        return linha + super(RegistroD359, self).gerar_linha()


class RegistroD500(Registro):
    '''
    Nota fiscal de serviço de comunicação (código 21) e nota fiscal de serviço
    de telecomunicação (código 22) - documentos de aquisicao com direito a
    crédito.
    '''

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D500"
        self.IND_OPER = ""
        self.IND_EMIT = ""
        self.COD_PART = ""
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.DT_DOC = ""
        self.DT_A_P = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.VL_SERV = ""
        self.VL_SERV_NT = ""
        self.VL_TERC = ""
        self.VL_DA = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.COD_INF = ""
        self.VL_PIS = ""
        self.VL_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.IND_EMIT,
            self.COD_PART,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.DT_DOC,
            self.DT_A_P,
            self.VL_DOC,
            self.VL_DESC,
            self.VL_SERV,
            self.VL_SERV_NT,
            self.VL_TERC,
            self.VL_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.COD_INF,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroD500, self).gerar_linha()


class RegistroD501(Registro):
    '''Complemento da operação (códigos 21 e 22) - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "D500"
        self.REG = "D501"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.VL_ITEM,
            self.NAT_BC_CRED,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD501, self).gerar_linha()


class RegistroD505(Registro):
    '''Complemento da operação (códigos 21 e 22) - Cofins'''

    def __init__(self):
        self.REG_PAI = "D500"
        self.REG = "D505"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.VL_ITEM,
            self.NAT_BC_CRED,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD505, self).gerar_linha()


class RegistroD509(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "D500"
        self.REG = "D509"
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
        return linha + super(RegistroD509, self).gerar_linha()


class RegistroD600(Registro):
    '''
    Consolidação da prestação de serviços - Notas de serviço de comunicação
    (código 21) e de serviço de telecomunicação (código 22)
    '''

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D600"
        self.COD_MOD = ""
        self.COD_MUN = ""
        self.SER = ""
        self.SUB = ""
        self.IND_REC = ""
        self.QTD_CONS = ""
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.VL_SERV = ""
        self.VL_SERV_NT = ""
        self.VL_TERC = ""
        self.VL_DA = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.VL_PIS = ""
        self.VL_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_MUN,
            self.SER,
            self.SUB,
            self.IND_REC,
            self.QTD_CONS,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.VL_DOC,
            self.VL_DESC,
            self.VL_SERV,
            self.VL_SERV_NT,
            self.VL_TERC,
            self.VL_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroD600, self).gerar_linha()


class RegistroD601(Registro):
    '''
    Complemento da consolidação da prestação de serviços (códigos 21 e 22)
    PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "D600"
        self.REG = "D601"
        self.COD_CLASS = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CLASS,
            self.VL_ITEM,
            self.VL_DESC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD601, self).gerar_linha()


class RegistroD605(Registro):
    '''
    Complemento da consolidação da prestação de serviços (códigos 21 e 22) -
    Cofins
    '''

    def __init__(self):
        self.REG_PAI = "D600"
        self.REG = "D605"
        self.COD_CLASS = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CLASS,
            self.VL_ITEM,
            self.VL_DESC,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD605, self).gerar_linha()


class RegistroD609(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "D600"
        self.REG = "D609"
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
        return linha + super(RegistroD609, self).gerar_linha()


class RegistroD990(RegistroX990):
    '''Encerramento do bloco D'''

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "D990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.QTD_LIN))
        return linha + super(RegistroD990, self).gerar_linha()
