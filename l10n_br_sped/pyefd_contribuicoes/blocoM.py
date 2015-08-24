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
from util import Ocorrencia, Obrigatoriedade
from RegistroX990 import RegistroX990


class RegistroM001(RegistroX001):
    '''Abertura do bloco M'''

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "M001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(RegistroM001, self).gerar_linha()


class RegistroM100(Registro):
    '''Crédito de PIS/PASEP relativo ao período'''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M100"
        self.COD_CRED = "101"
        self.IND_CRED_ORI = "0"
        self.VL_BC_PIS = "158"
        self.ALIQ_PIS = "1,65"
        self.QUANT_BC_PIS = "0"
        self.ALIQ_PIS_QTDE = ""
        self.VL_CRED = "2,61"
        self.VL_AJUS_ACRES = "0"
        self.VL_AJUS_REDUC = "0"
        self.VL_CRED_DIF = "0"
        self.VL_CRED_DISP = "2,61"
        self.IND_DESC_CRED = "1"
        self.VL_CRED_DESC = "0"
        self.SLD_CRED = "2,61"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CRED,
            self.IND_CRED_ORI,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QTDE,
            self.VL_CRED,
            self.VL_AJUS_ACRES,
            self.VL_AJUS_REDUC,
            self.VL_CRED_DIF,
            self.VL_CRED_DISP,
            self.IND_DESC_CRED,
            self.VL_CRED_DESC,
            self.SLD_CRED,
            ))
        return linha + super(RegistroM100, self).gerar_linha()


class RegistroM105(Registro):
    '''
    Detalhamento da base de cálculo do crédito apurado no período PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "M100"
        self.REG = "M105"
        self.NAT_BC_CRED = "01"
        self.CST_PIS = "50"
        self.VL_BC_PIS_TOT = "158"
        self.VL_BC_PIS_CUM = ""
        self.VL_BC_PIS_NC = "158"
        self.VL_BC_PIS = "158"
        self.QUANT_BC_PIS_TOT = ""
        self.QUANT_BC_PIS = "0"
        self.DESC_CRED = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.CST_PIS,
            self.VL_BC_PIS_TOT,
            self.VL_BC_PIS_CUM,
            self.VL_BC_PIS_NC,
            self.VL_BC_PIS,
            self.QUANT_BC_PIS_TOT,
            self.QUANT_BC_PIS,
            self.DESC_CRED,
            ))
        return linha + super(RegistroM105, self).gerar_linha()


class RegistroM110(Registro):
    '''Ajuste do crédito de PIS/PASEP apurado'''

    def __init__(self):
        self.REG_PAI = "M100"
        self.REG = "M110"
        self.IND_AJ = ""
        self.VL_AJ = ""
        self.COD_AJ = ""
        self.NUM_DOC = ""
        self.DESCR_AJ = ""
        self.DT_REF = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_AJ,
            self.VL_AJ,
            self.COD_AJ,
            self.NUM_DOC,
            self.DESCR_AJ,
            self.DT_REF,
            ))
        return linha + super(RegistroM110, self).gerar_linha()


class RegistroM200(Registro):
    '''Consolidação da contribuição para o PIS/PASEP do período'''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M200"
        self.ER = "0"
        self.VL_TOT_CRED_DESC = "0"
        self.VL_TOT_CRED_DESC_ANT = "0"
        self.VL_TOT_CONT_NC_DEV = "0"
        self.VL_RET_NC = "0"
        self.VL_OUT_DED_NC = "0"
        self.VL_CONT_NC_REC = "0"
        self.VL_TOT_CONT_CUM_PER = "0"
        self.VL_RET_CUM = "0"
        self.VL_OUT_DED_CUM = "0"
        self.VL_CONT_CUM_REC = "0"
        self.VL_TOT_CONT_REC = "0"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.ER,
            self.VL_TOT_CRED_DESC,
            self.VL_TOT_CRED_DESC_ANT,
            self.VL_TOT_CONT_NC_DEV,
            self.VL_RET_NC,
            self.VL_OUT_DED_NC,
            self.VL_CONT_NC_REC,
            self.VL_TOT_CONT_CUM_PER,
            self.VL_RET_CUM,
            self.VL_OUT_DED_CUM,
            self.VL_CONT_CUM_REC,
            self.VL_TOT_CONT_REC,
            ))
        return linha + super(RegistroM200, self).gerar_linha()


class RegistroM210(Registro):
    '''
    Detalhamento da contribuição para o PIS/PASEP do período.

    FIXME:
    Obs.: no layout, este registro esta como obrigatório. Porem,
          não foi necessario preenche-lo para passar no validador.
          Portanto, provisoriamente, está como OC.
    '''

    def __init__(self):
        self.REG_PAI = "M200"
        self.REG = "M210"
        self.COD_CONT = ""
        self.VL_REC_BRT = ""
        self.VL_BC_CONT = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_CONT_APUR = ""
        self.VL_AJUS_ACRES = ""
        self.VL_AJUS_REDUC = ""
        self.VL_CONT_DIFER = ""
        self.VL_CONT_DIFER_ANT = ""
        self.VL_CONT_PER = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # no layout esta como obrigatorio
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CONT,
            self.VL_REC_BRT,
            self.VL_BC_CONT,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_CONT_APUR,
            self.VL_AJUS_ACRES,
            self.VL_AJUS_REDUC,
            self.VL_CONT_DIFER,
            self.VL_CONT_DIFER_ANT,
            self.VL_CONT_PER,
            ))
        return linha + super(RegistroM210, self).gerar_linha()


class RegistroM211(Registro):
    '''Sociedades cooperativas - composição da base de cálculo - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "M210"
        self.REG = "M211"
        self.IND_TIP_COOP = ""
        self.VL_BC_CONT_ANT_EXC_COOP = ""
        self.VL_EXC_COOP_GER = ""
        self.VL_EXC_ESP_COOP = ""
        self.VL_BC_CONT = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        self.obrigatoriedade = Obrigatoriedade.O_SE

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_TIP_COOP,
            self.VL_BC_CONT_ANT_EXC_COOP,
            self.VL_EXC_COOP_GER,
            self.VL_EXC_ESP_COOP,
            self.VL_BC_CONT
            ))
        return linha + super(RegistroM211, self).gerar_linha()


class RegistroM220(Registro):
    '''Ajustes da contribuição para o PIS/PASEP apurada'''

    def __init__(self):
        self.REG_PAI = "M210"
        self.REG = "M220"
        self.IND_AJ = ""
        self.VL_AJ = ""
        self.COD_AJ = ""
        self.NUM_DOC = ""
        self.DESCR_AJ = ""
        self.DT_REF = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_AJ,
            self.VL_AJ,
            self.COD_AJ,
            self.NUM_DOC,
            self.DESCR_AJ,
            self.DT_REF
            ))
        return linha + super(RegistroM220, self).gerar_linha()


class RegistroM230(Registro):
    '''Informações adicionais de diferimento'''

    def __init__(self):
        self.REG_PAI = "M210"
        self.REG = "M230"
        self.CNPJ = ""
        self.VL_VEND = ""
        self.VL_NAO_RECEB = ""
        self.VL_CONT_DIF = ""
        self.VL_CRED_DIF = ""
        self.COD_CRED = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.VL_VEND,
            self.VL_NAO_RECEB,
            self.VL_CONT_DIF,
            self.VL_CRED_DIF,
            self.COD_CRED,
            ))
        return linha + super(Registro, self).gerar_linha()


class RegistroM300(Registro):
    '''
    Contribuição de PIS/PASEP diferida em períodos anteriores
    Valores a pagar no período
    '''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M300"
        self.COD_CONT = ""
        self.VL_CONT_REC = ""
        self.NAT_CRED_DESC = ""
        self.VL_CRED_DESC = ""
        self.PER_APUR = ""
        self.DT_RECEB = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CONT,
            self.VL_CONT_REC,
            self.NAT_CRED_DESC,
            self.VL_CRED_DESC,
            self.PER_APUR,
            self.DT_RECEB,
            ))
        return linha + super(RegistroM300, self).gerar_linha()


class RegistroM350(Registro):
    '''PIS/PASEP - Folha de salários'''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M350"
        self.VL_TOT_FOL = ""
        self.VL_EXC_BC = ""
        self.VL_TOT_BC = ""
        self.ALIQ_PIS_FOL = ""
        self.VL_TOT_CONT_FOL = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_TOT_FOL,
            self.VL_EXC_BC,
            self.VL_TOT_BC,
            self.ALIQ_PIS_FOL,
            self.VL_TOT_CONT_FOL,
            ))
        return linha + super(RegistroM350, self).gerar_linha()


class RegistroM400(Registro):
    '''
    Receitas isentas, não alcançadas pela incidência da contribuição, sujeitas
    a alíquota zero ou de vendas com suspensão - PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M400"
        self.CST_PIS = ""
        self.VL_TOT_REC = ""
        self.COD_CTA = ""
        self.DESC_COMPL = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.VL_TOT_REC,
            self.COD_CTA,
            self.DESC_COMPL,
            ))
        return linha + super(RegistroM400, self).gerar_linha()


class RegistroM410(Registro):
    '''
    Detalhamento das receitas isentas, não alcançadas pela incidência da
    contribuição, sujeitas a alíquota zero ou de vendas com suspensão -
    PIS/PASEP

    FIXME:
    Obs.: no layout, o campo 5 esta vazio.
    '''

    def __init__(self):
        self.REG_PAI = "M400"
        self.REG = "M410"
        self.NAT_REC = ""
        self.VL_REC = ""
        self.COD_CTA = ""
        self.DESC_COMPL = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se existir M400
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_REC,
            self.VL_REC,
            self.COD_CTA,
            self.DESC_COMPL,
            ))
        return linha + super(RegistroM410, self).gerar_linha()


class RegistroM500(Registro):
    '''Crédito de COFINS relativo ao período'''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M500"
        self.COD_CRED = "101"
        self.IND_CRED_ORI = "0"
        self.VL_BC_COFINS = "158"
        self.ALIQ_COFINS = "7,6"
        self.QUANT_BC_COFINS = "0"
        self.ALIQ_COFINS_QTDE = ""
        self.VL_CRED = "12,01"
        self.VL_AJUS_ACRES = "0"
        self.VL_AJUS_REDUC = "0"
        self.VL_CRED_DIF = "0"
        self.VL_CRED_DISP = "12,01"
        self.IND_DESC_CRED = "1"
        self.VL_CRED_DESC = "0"
        self.SLD_CRED = "12,01"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CRED,
            self.IND_CRED_ORI,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QTDE,
            self.VL_CRED,
            self.VL_AJUS_ACRES,
            self.VL_AJUS_REDUC,
            self.VL_CRED_DIF,
            self.VL_CRED_DISP,
            self.IND_DESC_CRED,
            self.VL_CRED_DESC,
            self.SLD_CRED,
            ))
        return linha + super(RegistroM500, self).gerar_linha()


class RegistroM505(Registro):
    '''
    Detalhamento da base de cálculo do crédito apurado no período - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "M500"
        self.REG = "M505"
        self.NAT_BC_CRED = "01"
        self.CST_COFINS = "50"
        self.VL_BC_COFINS_TOT = "158"
        self.VL_BC_COFINS_CUM = ""
        self.VL_BC_COFINS_NC = "158"
        self.VL_BC_COFINS = "158"
        self.QUANT_BC_COFINS_TOT = ""
        self.QUANT_BC_COFINS = "0"
        self.DESC_CRED = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.CST_COFINS,
            self.VL_BC_COFINS_TOT,
            self.VL_BC_COFINS_CUM,
            self.VL_BC_COFINS_NC,
            self.VL_BC_COFINS,
            self.QUANT_BC_COFINS_TOT,
            self.QUANT_BC_COFINS,
            self.DESC_CRED,
            ))
        return linha + super(RegistroM505, self).gerar_linha()


class RegistroM510(Registro):
    '''Ajustes do crédito de Cofins apurado'''

    def __init__(self):
        self.REG_PAI = "M500"
        self.REG = "M510"
        self.IND_AJ = ""
        self.VL_AJ = ""
        self.COD_AJ = ""
        self.NUM_DOC = ""
        self.DESCR_AJ = ""
        self.DT_REF = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_AJ,
            self.VL_AJ,
            self.COD_AJ,
            self.NUM_DOC,
            self.DESCR_AJ,
            self.DT_REF,
            ))
        return linha + super(RegistroM510, self).gerar_linha()


class RegistroM600(Registro):
    '''Consolidação da contribuição para a seguridade social'''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M600"
        self.VL_TOT_CONT_NC_PER = "0"
        self.VL_TOT_CRED_DESC = "0"
        self.VL_TOT_CRED_DESC_ANT = "0"
        self.VL_TOT_CONT_NC_DEV = "0"
        self.VL_RET_NC = "0"
        self.VL_OUT_DED_NC = "0"
        self.VL_CONT_NC_REC = "0"
        self.VL_TOT_CONT_CUM_PER = "0"
        self.VL_RET_CUM = "0"
        self.VL_OUT_DED_CUM = "0"
        self.VL_CONT_CUM_REC = "0"
        self.VL_TOT_CONT_REC = "0"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_TOT_CONT_NC_PER,
            self.VL_TOT_CRED_DESC,
            self.VL_TOT_CRED_DESC_ANT,
            self.VL_TOT_CONT_NC_DEV,
            self.VL_RET_NC,
            self.VL_OUT_DED_NC,
            self.VL_CONT_NC_REC,
            self.VL_TOT_CONT_CUM_PER,
            self.VL_RET_CUM,
            self.VL_OUT_DED_CUM,
            self.VL_CONT_CUM_REC,
            self.VL_TOT_CONT_REC,
            ))
        return linha + super(RegistroM600, self).gerar_linha()


class RegistroM610(Registro):
    '''
    Detalhamento da contribuição para a seguridade social - Cofins do período.

    Obs.: no layout, este registro esta como obrigatorio. Porem,
          não foi necessario preenche-lo para passar no validador.
          Portanto, provisoriamente, esta como OC.
    '''

    def __init__(self):
        self.REG_PAI = "M600"
        self.REG = "M610"
        self.COD_CONT = ""
        self.VL_REC_BRT = ""
        self.VL_BC_CONT = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_CONT_APUR = ""
        self.VL_AJUS_ACRES = ""
        self.VL_AJUS_REDUC = ""
        self.VL_CONT_DIFER = ""
        self.VL_CONT_DIFER_ANT = ""
        self.VL_CONT_PER = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # no layout esta como obrigatorio
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CONT,
            self.VL_REC_BRT,
            self.VL_BC_CONT,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_CONT_APUR,
            self.VL_AJUS_ACRES,
            self.VL_AJUS_REDUC,
            self.VL_CONT_DIFER,
            self.VL_CONT_DIFER_ANT,
            self.VL_CONT_PER,
            ))
        return linha + super(RegistroM610, self).gerar_linha()


class RegistroM611(Registro):
    '''Sociedades cooperativas - Composição da base de cálculo - Cofins'''

    def __init__(self):
        self.REG_PAI = "M610"
        self.REG = "M611"
        self.IND_TIP_COOP = ""
        self.VL_BC_CONT_ANT_E_XC_COOP = ""
        self.VL_EXC_COOP_GER = ""
        self.VL_EXC_ESP_COOP = ""
        self.VL_BC_CONT = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        # se IND_NAT_PJ do registro 0000 for igual a 01
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_TIP_COOP,
            self.VL_BC_CONT_ANT_E_XC_COOP,
            self.VL_EXC_COOP_GER,
            self.VL_EXC_ESP_COOP,
            self.VL_BC_CONT,
            ))
        return linha + super(RegistroM611, self).gerar_linha()


class RegistroM620(Registro):
    '''Ajustes da Cofins apurada'''

    def __init__(self):
        self.REG_PAI = "M610"
        self.REG = "M620"
        self.IND_AJ = ""
        self.VL_AJ = ""
        self.COD_AJ = ""
        self.NUM_DOC = ""
        self.DESCR_AJ = ""
        self.DT_REF = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_AJ,
            self.VL_AJ,
            self.COD_AJ,
            self.NUM_DOC,
            self.DESCR_AJ,
            self.DT_REF,
            ))
        return linha + super(RegistroM620, self).gerar_linha()


class RegistroM630(Registro):
    '''Informações adicionais de diferimento'''

    def __init__(self):
        self.REG_PAI = "M610"
        self.REG = "M630"
        self.CNPJ = ""
        self.VL_VEND = ""
        self.VL_NAO_RECEB = ""
        self.VL_CONT_DIF = ""
        self.VL_CRED_DIF = ""
        self.COD_CRED = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.VL_VEND,
            self.VL_NAO_RECEB,
            self.VL_CONT_DIF,
            self.VL_CRED_DIF,
            self.COD_CRED,
            ))
        return linha + super(RegistroM630, self).gerar_linha()


class RegistroM700(Registro):
    '''Cofins diferida em períodos anteriores - Valores a pagar no período'''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M700"
        self.COD_CONT = ""
        self.VL_CONT_REC = ""
        self.NAT_CRED_DESC = ""
        self.VL_CRED_DESC = ""
        self.PER_APUR = ""
        self.DT_RECEB = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CONT,
            self.VL_CONT_REC,
            self.NAT_CRED_DESC,
            self.VL_CRED_DESC,
            self.PER_APUR,
            self.DT_RECEB,
            ))
        return linha + super(RegistroM700, self).gerar_linha()


class RegistroM800(Registro):
    '''
    Receitas isentas, não alcançadas pela incidência da contribuição, sujeitas
    a alíquota zero ou de vendas com suspensão - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "M001"
        self.REG = "M800"
        self.CST_COFINS = ""
        self.VL_TOT_REC = ""
        self.COD_CTA = ""
        self.DESC_COMPL = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.VL_TOT_REC,
            self.COD_CTA,
            self.DESC_COMPL,
            ))
        return linha + super(RegistroM800, self).gerar_linha()


class RegistroM810(Registro):
    '''
    Detalhamento das receitas isentas, não alcançadas pela incidência da
    contribuição, sujeitas a alíquota zero ou de vendas com suspensão - Cofins.

    FIXME:
    Obs.: no layout, esta faltando o campo 3 ?
    '''

    def __init__(self):
        self.REG_PAI = "M800"
        self.REG = "M810"
        self.NAT_REC = ""
        self.VL_REC = ""
        self.COD_CTA = ""
        self.DESC_COMPL = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se existir M800
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_REC,
            self.VL_REC,
            self.COD_CTA,
            self.DESC_COMPL,
            ))
        return linha + super(RegistroM810, self).gerar_linha()


class RegistroM990(RegistroX990):
    '''Encerramento do bloco M'''

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "M990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(RegistroM990, self).gerar_linha()
