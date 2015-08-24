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

from Registro import Registro, RegistroX001
from RegistroX990 import RegistroX990
from util import Ocorrencia, Obrigatoriedade


class Registro1001(RegistroX001):
    ''' Abertura do bloco 1'''

    def __init__(self):
        super(Registro1001, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "1001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(Registro1001, self).gerar_linha()


class Registro1010(Registro):
    '''Processo referenciado - Ação judicial'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1010"
        self.NUM_PROC = ""
        self.ID_SEC_JUD = ""
        self.ID_VARA = ""
        self.IND_NAT_ACAO = ""
        self.DESC_DEC_JUD = ""
        self.DT_SENT_JUD = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.ID_SEC_JUD,
            self.ID_VARA,
            self.IND_NAT_ACAO,
            self.DESC_DEC_JUD,
            self.DT_SENT_JUD,
            ))
        return linha + super(Registro1010, self).gerar_linha()


class Registro1020(Registro):
    '''Processo referenciado - Processo administrativo'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1020"
        self.NUM_PROC = ""
        self.IND_NAT_ACAO = ""
        self.DT_DEC_ADM = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_NAT_ACAO,
            self.DT_DEC_ADM,
            ))
        return linha + super(Registro1020, self).gerar_linha()


class Registro1100(Registro):
    '''Controle de créditos fiscais - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1100"
        self.PER_APU_CRED = ""
        self.ORIG_CRED = ""
        self.CNPJ_SUC = ""
        self.COD_CRED = ""
        self.VL_CRED_APU = ""
        self.VL_CRED_EXT_APU = ""
        self.VL_TOT_CRED_APU = ""
        self.VL_CRED_DESC_PA_ANT = ""
        self.VL_CRED_PER_PA_ANT = ""
        self.VL_CRED_DCOMP_PA_ANT = ""
        self.SD_CRED_DISP_EFD = ""
        self.VL_CRED_DESC_EFD = ""
        self.VL_CRED_PER_EFD = ""
        self.VL_CRED_DCOMP_EFD = ""
        self.VL_CRED_TRANS = ""
        self.VL_CRED_OUT = ""
        self.SLD_CRED_FIM = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_APU_CRED,
            self.ORIG_CRED,
            self.CNPJ_SUC,
            self.COD_CRED,
            self.VL_CRED_APU,
            self.VL_CRED_EXT_APU,
            self.VL_TOT_CRED_APU,
            self.VL_CRED_DESC_PA_ANT,
            self.VL_CRED_PER_PA_ANT,
            self.VL_CRED_DCOMP_PA_ANT,
            self.SD_CRED_DISP_EFD,
            self.VL_CRED_DESC_EFD,
            self.VL_CRED_PER_EFD,
            self.VL_CRED_DCOMP_EFD,
            self.VL_CRED_TRANS,
            self.VL_CRED_OUT,
            self.SLD_CRED_FIM,
            ))
        return linha + super(Registro1100, self).gerar_linha()


class Registro1101(Registro):
    '''
    Apuração de crédito extemporâneo - Documentos e operações de periodos
    anteriores - PIS/PASEP.
    '''

    def __init__(self):
        self.REG_PAI = "1100"
        self.REG = "1101"
        self.COD_PART = ""
        self.COD_ITEM = ""
        self.COD_MOD = ""
        self.SER = ""
        self.SUB_SER = ""
        self.NUM_DOC = ""
        self.DT_OPER = ""
        self.CHV_NFE = ""
        self.VL_OPER = ""
        self.CFOP = ""
        self.NAT_BC_CRED = ""
        self.IND_ORIG_CRED = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_COMPL = ""
        self.PER_ESCRIT = ""
        self.CNPJ = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se VL_CRED_EXT_APU do registro 1100 > 0
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.COD_ITEM,
            self.COD_MOD,
            self.SER,
            self.SUB_SER,
            self.NUM_DOC,
            self.DT_OPER,
            self.CHV_NFE,
            self.VL_OPER,
            self.CFOP,
            self.NAT_BC_CRED,
            self.IND_ORIG_CRED,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_COMPL,
            self.PER_ESCRIT,
            self.CNPJ,
            ))
        return linha + super(Registro1101, self).gerar_linha()


class Registro1102(Registro):
    '''
    Detalhamento do crédito extemporâneo vinculado a mais de um tipo de receita
    - PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "1101"
        self.REG = "1102"
        self.VL_CRED_PIS_TRIB_MI = ""
        self.VL_CRED_PIS_NT_MI = ""
        self.VL_CRED_PIS_EXP = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se CST_PIS do registro 1101 for 53, 54, 55, 56, 63, 64, 65 ou 66
        self.obrigatoriedade = Obrigatoriedade.O_SE

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_CRED_PIS_TRIB_MI,
            self.VL_CRED_PIS_NT_MI,
            self.VL_CRED_PIS_EXP,
            ))
        return linha + super(Registro1102, self).gerar_linha()


class Registro1200(Registro):
    '''Contribuição social extemporânea - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1200"
        self.PER_APUR_ANT = ""
        self.NAT_CONT_REC = ""
        self.VL_CONT_APUR = ""
        self.VL_CRED_PIS_DESC = ""
        self.VL_CONT_DEV = ""
        self.VL_OUT_DED = ""
        self.VL_CONT_EXT = ""
        self.VL_MUL = ""
        self.VL_JUR = ""
        self.DT_RECOL = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_APUR_ANT,
            self.NAT_CONT_REC,
            self.VL_CONT_APUR,
            self.VL_CRED_PIS_DESC,
            self.VL_CONT_DEV,
            self.VL_OUT_DED,
            self.VL_CONT_EXT,
            self.VL_MUL,
            self.VL_JUR,
            self.DT_RECOL,
            ))
        return linha + super(Registro1200, self).gerar_linha()


class Registro1210(Registro):
    '''Detalhamento da contribuição social extemporânea - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "1200"
        self.REG = "1210"
        self.CNPJ = ""
        self.CST_PIS = ""
        self.COD_PART = ""
        self.DT_OPER = ""
        self.VL_OPER = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.DESC_COMPL = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se existir registro 1200
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.CST_PIS,
            self.COD_PART,
            self.DT_OPER,
            self.VL_OPER,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            self.DESC_COMPL,
            ))
        return linha + super(Registro1210, self).gerar_linha()


class Registro1220(Registro):
    '''
    Demonstração do crédito a descontar da contribuição extemporânea -
    PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "1200"
        self.REG = "1220"
        self.PER_APU_CRED = ""
        self.ORIG_CRED = ""
        self.COD_CRED = ""
        self.VL_CRED = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_APU_CRED,
            self.ORIG_CRED,
            self.COD_CRED,
            self.VL_CRED,
            ))
        return linha + super(Registro1220, self).gerar_linha()


class Registro1300(Registro):
    '''Controle dos valores retidos na fonte - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1300"
        self.IND_NAT_RET = ""
        self.PR_REC_RET = ""
        self.VL_RET_APU = ""
        self.VL_RET_DED = ""
        self.VL_RET_PER = ""
        self.VL_RET_DCOMP = ""
        self.SLD_RET = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_RET,
            self.PR_REC_RET,
            self.VL_RET_APU,
            self.VL_RET_DED,
            self.VL_RET_PER,
            self.VL_RET_DCOMP,
            self.SLD_RET,
            ))
        return linha + super(Registro1300, self).gerar_linha()


class Registro1500(Registro):
    '''Controle de créditos fiscais - Cofins'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1500"
        self.PER_APU_CRED = ""
        self.ORIG_CRED = ""
        self.CNPJ_SUC = ""
        self.COD_CRED = ""
        self.VL_CRED_APU = ""
        self.VL_CRED_EXT_APU = ""
        self.VL_TOT_CRED_APU = ""
        self.VL_CRED_DESC_PA_ANT = ""
        self.VL_CRED_PER_PA_ANT = ""
        self.VL_CRED_DCOMP_PA_ANT = ""
        self.SD_CRED_DISP_EFD = ""
        self.VL_CRED_DESC_EFD = ""
        self.VL_CRED_PER_EFD = ""
        self.VL_CRED_DCOMP_EFD = ""
        self.VL_CRED_TRANS = ""
        self.VL_CRED_OUT = ""
        self.SLD_CRED_FIM = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_APU_CRED,
            self.ORIG_CRED,
            self.CNPJ_SUC,
            self.COD_CRED,
            self.VL_CRED_APU,
            self.VL_CRED_EXT_APU,
            self.VL_TOT_CRED_APU,
            self.VL_CRED_DESC_PA_ANT,
            self.VL_CRED_PER_PA_ANT,
            self.VL_CRED_DCOMP_PA_ANT,
            self.SD_CRED_DISP_EFD,
            self.VL_CRED_DESC_EFD,
            self.VL_CRED_PER_EFD,
            self.VL_CRED_DCOMP_EFD,
            self.VL_CRED_TRANS,
            self.VL_CRED_OUT,
            self.SLD_CRED_FIM,
            ))
        return linha + super(Registro1500, self).gerar_linha()


class Registro1501(Registro):
    '''
    Apuração de crédito extemporâneo - Documentos e operações de periodos
    anteriores Cofins
    '''

    def __init__(self):
        self.REG_PAI = "1500"
        self.REG = "1501"
        self.COD_PART = ""
        self.COD_ITEM = ""
        self.COD_MOD = ""
        self.SER = ""
        self.SUB_SER = ""
        self.NUM_DOC = ""
        self.DT_OPER = ""
        self.CHV_NFE = ""
        self.VL_OPER = ""
        self.CFOP = ""
        self.NAT_BC_CRED = ""
        self.IND_ORIG_CRED = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_COMPL = ""
        self.PER_ESCRIT = ""
        self.CNPJ = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se VL_CRED_EXT_APU do registro 1500 > 0
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.COD_ITEM,
            self.COD_MOD,
            self.SER,
            self.SUB_SER,
            self.NUM_DOC,
            self.DT_OPER,
            self.CHV_NFE,
            self.VL_OPER,
            self.CFOP,
            self.NAT_BC_CRED,
            self.IND_ORIG_CRED,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_COMPL,
            self.PER_ESCRIT,
            self.CNPJ,
            ))
        return linha + super(Registro1501, self).gerar_linha()


class Registro1502(Registro):
    '''
    Detalhamento do crédito extemporâneo vinculado a mais de um tipo de receita
    - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "1501"
        self.REG = "1502"
        self.VL_CRED_COFINS_TRIB_MI = ""
        self.VL_CRED_COFINS_NT_MI = ""
        self.VL_CRED_COFINS_EXP = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM

        # se CST_COFINS do registro 1501 for 53, 54, 55, 56, 63, 64, 65 ou 66
        self.obrigatoriedade = Obrigatoriedade.O_SE

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_CRED_COFINS_TRIB_MI,
            self.VL_CRED_COFINS_NT_MI,
            self.VL_CRED_COFINS_EXP,
            ))
        return linha + super(Registro1502, self).gerar_linha()


class Registro1600(Registro):
    '''Contribuição social extemporânea - Cofins'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1600"
        self.PER_APUR_ANT = ""
        self.NAT_CONT_REC = ""
        self.VL_CONT_APUR = ""
        self.VL_CRED_COFINS_DESC = ""
        self.VL_CONT_DEV = ""
        self.VL_OUT_DED = ""
        self.VL_CONT_EXT = ""
        self.VL_MUL = ""
        self.VL_JUR = ""
        self.DT_RECOL = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_APUR_ANT,
            self.NAT_CONT_REC,
            self.VL_CONT_APUR,
            self.VL_CRED_COFINS_DESC,
            self.VL_CONT_DEV,
            self.VL_OUT_DED,
            self.VL_CONT_EXT,
            self.VL_MUL,
            self.VL_JUR,
            self.DT_RECOL,
            ))
        return linha + super(Registro1600, self).gerar_linha()


class Registro1610(Registro):
    '''Detalhamento da contribuição social extemporânea - Cofins'''

    def __init__(self):
        self.REG_PAI = "1600"
        self.REG = "1610"
        self.CNPJ = ""
        self.CST_COFINS = ""
        self.COD_PART = ""
        self.DT_OPER = ""
        self.VL_OPER = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.DESC_COMPL = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se existir 1600
        self.obrigatoriedade = Obrigatoriedade.O_SE

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.CST_COFINS,
            self.COD_PART,
            self.DT_OPER,
            self.VL_OPER,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.DESC_COMPL,
            ))
        return linha + super(Registro1610, self).gerar_linha()


class Registro1620(Registro):
    '''
    Demonstração do crédito a descontar da contribuição extemporânea - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "1600"
        self.REG = "1620"
        self.PER_APU_CRED = ""
        self.ORIG_CRED = ""
        self.COD_CRED = ""
        self.VL_CRED = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_APU_CRED,
            self.ORIG_CRED,
            self.COD_CRED,
            self.VL_CRED,
            ))
        return linha + super(Registro1620, self).gerar_linha()


class Registro1700(Registro):
    '''Controle dos valores retidos na fonte - Cofins'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1700"
        self.IND_NAT_RET = ""
        self.PR_REC_RET = ""
        self.VL_RET_APU = ""
        self.VL_RET_DED = ""
        self.VL_RET_PER = ""
        self.VL_RET_DCOMP = ""
        self.SLD_RET = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_RET,
            self.PR_REC_RET,
            self.VL_RET_APU,
            self.VL_RET_DED,
            self.VL_RET_PER,
            self.VL_RET_DCOMP,
            self.SLD_RET,
            ))
        return linha + super(Registro1700, self).gerar_linha()


class Registro1800(Registro):
    '''Incorporação imobiliária - RET'''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1800"
        self.INC_IMOB = ""
        self.REC_RECEB_RET = ""
        self.REC_FIN_RET = ""
        self.BC_RET = ""
        self.ALIQ_RET = ""
        self.VL_REC_UNI = ""
        self.DT_REC_UNI = ""
        self.COD_REC = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.INC_IMOB,
            self.REC_RECEB_RET,
            self.REC_FIN_RET,
            self.BC_RET,
            self.ALIQ_RET,
            self.VL_REC_UNI,
            self.DT_REC_UNI,
            self.COD_REC,
            ))
        return linha + super(Registro1800, self).gerar_linha()


class Registro1809(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "1800"
        self.REG = "1809"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(Registro1809, self).gerar_linha()


class Registro1900(Registro):
    '''
    Consolidação dos Documentos Emitidos por Pessoa Jurídica Submetida ao
    Regime de Tributação com Base no Lucro Presumido - Regime de Caixa ou de
    Competência
    '''

    def __init__(self):
        self.REG_PAI = "1001"
        self.REG = "1900"
        self.CNPJ = ''
        self.COD_MOD = ''
        self.SER = ''
        self.SUB_SER = ''
        self.COD_SIT = ''
        self.VL_TOT_REC = ''
        self.QUANT_DOC = ''
        self.CST_PIS = ''
        self.CST_COFINS = ''
        self.CFOP = ''
        self.INF_COMPL = ''
        self.COD_CTA = ''
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.COD_MOD,
            self.SER,
            self.SUB_SER,
            self.COD_SIT,
            self.VL_TOT_REC,
            self.QUANT_DOC,
            self.CST_PIS,
            self.CST_COFINS,
            self.CFOP,
            self.INF_COMPL,
            self.COD_CTA,
            ))
        return linha + super(Registro1900, self).gerar_linha()


class Registro1990(RegistroX990):
    '''Encerramento do bloco 1'''

    def __init__(self):
        super(Registro1990, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "1990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.QTD_LIN))
        return linha + super(Registro1990, self).gerar_linha()
