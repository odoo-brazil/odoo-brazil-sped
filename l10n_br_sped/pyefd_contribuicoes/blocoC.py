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

from Registro import RegistroX001, Registro
from RegistroX990 import RegistroX990
from util import Obrigatoriedade, Ocorrencia


class RegistroC001(RegistroX001):
    '''Abertura do bloco C'''

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "C001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(RegistroC001, self).gerar_linha()


class RegistroC010(Registro):
    '''Identificação do estabelecimento'''

    def __init__(self):
        self.REG_PAI = "C001"
        self.REG = "C010"
        self.CNPJ = "22222222000191"
        self.IND_ESCRI = "2"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.IND_ESCRI,
            ))
        return linha + super(RegistroC010, self).gerar_linha()


class RegistroC100(Registro):
    '''
    Documento - Nota Fiscal (Código 01), Nota Fiscal Avulsa (Código 1B),
                Nota Fiscal de Produtor (Código 04) e NFe (Código 55).
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C100"
        self.IND_OPER = "0"
        self.IND_EMIT = "1"
        self.COD_PART = "122"
        self.COD_MOD = "55"
        self.COD_SIT = "00"
        self.SER = "2"
        self.NUM_DOC = "8038"
        self.CHV_NFE = ""
        self.DT_DOC = "03012011"
        self.DT_E_S = "03012011"
        self.VL_DOC = "316,00"
        self.IND_PGTO = "1"
        self.VL_DESC = "0,00"
        self.VL_ABAT_NT = "0,00"
        self.VL_MERC = "316,00"
        self.IND_FRT = "1"
        self.VL_FRT = "0,00"
        self.VL_SEG = "0,00"
        self.VL_OUT_DA = "0,00"
        self.VL_BC_ICMS = "0,00"
        self.VL_ICMS = "0,00"
        self.VL_BC_ICMS_ST = "316,00"
        self.VL_ICMS_ST = "316,00"
        self.VL_IPI = "0,00"
        self.VL_PIS = "2,61"
        self.VL_COFINS = "12,01"
        self.VL_PIS_ST = "0,00"
        self.VL_COFINS_ST = "0,00"
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
            self.NUM_DOC,
            self.CHV_NFE,
            self.DT_DOC,
            self.DT_E_S,
            self.VL_DOC,
            self.IND_PGTO,
            self.VL_DESC,
            self.VL_ABAT_NT,
            self.VL_MERC,
            self.IND_FRT,
            self.VL_FRT,
            self.VL_SEG,
            self.VL_OUT_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_BC_ICMS_ST,
            self.VL_ICMS_ST,
            self.VL_IPI,
            self.VL_PIS,
            self.VL_COFINS,
            self.VL_PIS_ST,
            self.VL_COFINS_ST,
            ))
        return linha + super(RegistroC100, self).gerar_linha()


class RegistroC110(Registro):
    '''
    Complemento do documento - informação complementar da nota fiscal (códigos
    01, 1B, 04 e 55). Layout para este registro encontra-se no ATO COTEPE/ICMS
    No 9, DE 18 DE ABRIL DE 2008
    http://www.fazenda.gov.br/confaz/confaz/atos/atos_cotepe/2008/ac009_08.htm
    '''

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C110"
        self.COD_INF = ""
        self.TXT_COMPL = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_INF,
            self.TXT_COMPL,
            ))
        return linha + super(RegistroC110, self).gerar_linha()


class RegistroC111(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C111"
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
        return linha + super(RegistroC111, self).gerar_linha()


class RegistroC120(Registro):
    '''
    Complemento do documento - operações de importacao (código 01). Layout para
    este registro encontra-se no ATO COTEPE/ICMS No 9, DE 18 DE ABRIL DE 2008
    http://www.fazenda.gov.br/confaz/confaz/atos/atos_cotepe/2008/ac009_08.htm
    '''

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C120"
        self.COD_DOC_IMP = ""
        self.NUM_DOC_IMP = ""
        self.PIS_IMP = ""
        self.COFINS_IMP = ""
        self.NUM_ACDRAW = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_DOC_IMP,
            self.NUM_DOC_IMP,
            self.PIS_IMP,
            self.COFINS_IMP,
            self.NUM_ACDRAW,
            ))
        return linha + super(RegistroC120, self).gerar_linha()


class RegistroC170(Registro):
    '''
    Complemento do documento - Itens do documento (códigos 01, 1B, 04 e 55)
    '''

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C170"
        self.NUM_ITEM = "001"
        self.COD_ITEM = "1"
        self.DESCR_COMPL = ""
        self.QTD = "2,00000"
        self.UNID = "UN"
        self.VL_ITEM = "158,00"
        self.VL_DESC = "0,00"
        self.IND_MOV = "0"
        self.CST_ICMS = "060"
        self.CFOP = "1403"
        self.COD_NAT = "1403"
        self.VL_BC_ICMS = "158,00"
        self.ALIQ_ICMS = "18,00"
        self.VL_ICMS = "31,54"
        self.VL_BC_ICMS_ST = "0,00"
        self.ALIQ_ST = "0,00"
        self.VL_ICMS_ST = "0,00"
        self.IND_APUR = "0"
        self.CST_IPI = "02"
        self.COD_ENQ = ""
        self.VL_BC_IPI = "0,00"
        self.ALIQ_IPI = "0,00"
        self.VL_IPI = "0,00"
        self.CST_PIS = "50"
        self.VL_BC_PIS = "158,00"
        self.ALIQ_PIS_PERC = "1,65"
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_REAIS = ""
        self.VL_PIS = "2,61"
        self.CST_COFINS = "50"
        self.VL_BC_COFINS = "158,00"
        self.ALIQ_COFINS_PERC = "7,60"
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_REAIS = ""
        self.VL_COFINS = "12,01"
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_ITEM,
            self.COD_ITEM,
            self.DESCR_COMPL,
            self.QTD,
            self.UNID,
            self.VL_ITEM,
            self.VL_DESC,
            self.IND_MOV,
            self.CST_ICMS,
            self.CFOP,
            self.COD_NAT,
            self.VL_BC_ICMS,
            self.ALIQ_ICMS,
            self.VL_ICMS,
            self.VL_BC_ICMS_ST,
            self.ALIQ_ST,
            self.VL_ICMS_ST,
            self.IND_APUR,
            self.CST_IPI,
            self.COD_ENQ,
            self.VL_BC_IPI,
            self.ALIQ_IPI,
            self.VL_IPI,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS_PERC,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_REAIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS_PERC,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_REAIS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC170, self).gerar_linha()


class RegistroC180(Registro):
    '''
    Consolidação de notas fiscais eletrônicas emitidas pela pessoa juridica
    (código 55) - operações de vendas
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C180"
        self.COD_MOD = ""
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.COD_ITEM = ""
        self.COD_NCM = ""
        self.EX_IPI = ""
        self.VL_TOT_ITEM = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.COD_ITEM,
            self.COD_NCM,
            self.EX_IPI,
            self.VL_TOT_ITEM,
            ))
        return linha + super(RegistroC180, self).gerar_linha()


class RegistroC181(Registro):
    '''Detalhamento da consolidação - operações de vendas - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "C180"
        self.REG = "C181"
        self.CST_PIS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC181, self).gerar_linha()


class RegistroC185(Registro):
    '''Detalhamento da consolidação - operações de vendas - Cofins'''

    def __init__(self):
        self.REG_PAI = "C180"
        self.REG = "C185"
        self.CST_COFINS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC185, self).gerar_linha()


class RegistroC188(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C180"
        self.REG = "C188"
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
        return linha + super(RegistroC188, self).gerar_linha()


class RegistroC190(Registro):
    '''
    Consolidação de notas fiscais eletrônicas (código 55) - operações de
    aquisição com direito a crédito, e operações de devolução de compras e
    vendas
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C190"
        self.COD_MOD = ""
        self.DT_REF_INI = ""
        self.DT_REF_FIN = ""
        self.COD_ITEM = ""
        self.COD_NCM = ""
        self.EX_IPI = ""
        self.VL_TOT_ITEM = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.DT_REF_INI,
            self.DT_REF_FIN,
            self.COD_ITEM,
            self.COD_NCM,
            self.EX_IPI,
            self.VL_TOT_ITEM,
            ))
        return linha + super(RegistroC190, self).gerar_linha()


class RegistroC191(Registro):
    '''
    Detalhamento da consolidação - operações de aquisição com direito a
    crédito, e operações de devolução de compras e vendas - PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C191"
        self.COD_PART = ""
        self.CST_PIS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.CST_PIS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC191, self).gerar_linha()


class RegistroC195(Registro):
    '''
    Detalhamento da consolidação - operações de aquisição com direito a
    crédito, e operações de devolução de compras e vendas - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C195"
        self.COD_PART = ""
        self.CST_COFINS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.CST_COFINS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC195, self).gerar_linha()


class RegistroC198(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C198"
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
        return linha + super(RegistroC198, self).gerar_linha()


class RegistroC199(Registro):
    '''Complemento do documento - operações de importacao (códigos 55)'''

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C199"
        self.COD_DOC_IMP = ""
        self.NUM_DOC_IMP = ""
        self.VL_PIS_IMP = ""
        self.VL_COFINS_IMP = ""
        self.NUM_ACDRAW = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_DOC_IMP,
            self.NUM_DOC_IMP,
            self.VL_PIS_IMP,
            self.VL_COFINS_IMP,
            self.NUM_ACDRAW,
            ))
        return linha + super(RegistroC199, self).gerar_linha()


class RegistroC380(Registro):
    '''
    Nota fiscal de venda a consumidor (código 02) - consolidação de documentos
    emitidos
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C380"
        self.COD_MOD = ""
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.NUM_DOC_INI = ""
        self.NUM_DOC_FIN = ""
        self.VL_DOC = ""
        self.VL_DOC_CANC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.NUM_DOC_INI,
            self.NUM_DOC_FIN,
            self.VL_DOC,
            self.VL_DOC_CANC,
            ))
        return linha + super(RegistroC380, self).gerar_linha()


class RegistroC381(Registro):
    '''Detalhamento da consolidação - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "C380"
        self.REG = "C381"
        self.CST_PIS = ""
        self.COD_ITEM = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.COD_ITEM,
            self.VL_ITEM,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC381, self).gerar_linha()


class RegistroC385(Registro):
    '''Detalhamento da consolidação - Cofins'''

    def __init__(self):
        self.REG_PAI = "C380"
        self.REG = "C385"
        self.CST_COFINS = ""
        self.COD_ITEM = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.COD_ITEM,
            self.VL_ITEM,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC385, self).gerar_linha()


class RegistroC395(Registro):
    '''
    Notas fiscais de venda a consumidor (códigos 02, 2D, 2E e 59) - aquisições/
    entradas com crédito
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C395"
        self.COD_MOD = ""
        self.COD_PART = ""
        self.SER = ""
        self.SUB_SER = ""
        self.NUM_DOC = ""
        self.DT_DOC = ""
        self.VL_DOC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_PART,
            self.SER,
            self.SUB_SER,
            self.NUM_DOC,
            self.DT_DOC,
            self.VL_DOC,
            ))
        return linha + super(RegistroC395, self).gerar_linha()


class RegistroC396(Registro):
    '''
    Itens do documento (códigos 02, 2D, 2E e 59) - aquisições/entradas com
    crédito
    '''

    def __init__(self):
        self.REG_PAI = "C395"
        self.REG = "C396"
        self.COD_ITEM = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.NAT_BC_CRED = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.VL_ITEM,
            self.VL_DESC,
            self.NAT_BC_CRED,
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
        return linha + super(RegistroC396, self).gerar_linha()


class RegistroC400(Registro):
    '''Equipamento ECF (códigos 02 e 2D)'''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C400"
        self.COD_MOD = ""
        self.ECF_MOD = ""
        self.ECF_FAB = ""
        self.ECF_CX = ""
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
            self.ECF_CX,
            ))
        return linha + super(RegistroC400, self).gerar_linha()

    def preencher_valores_dos_campos_pela_linha(self, linha):
        valores = linha.split("\\|")
        self.COD_MOD = valores[2]
        self.ECF_MOD = valores[3]
        self.ECF_FAB = valores[4]
        self.ECF_CX = valores[5]


class RegistroC405(Registro):
    '''Redução Z (códigos 02 e 2D)'''

    def __init__(self):
        self.REG_PAI = "C400"
        self.REG = "C405"
        self.DT_DOC = ""
        self.CRO = ""
        self.CRZ = ""
        self.NUM_COO_FIN = ""
        self.GT_FIN = ""
        self.VL_BRT = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_DOC,
            self.CRO,
            self.CRZ,
            self.NUM_COO_FIN,
            self.GT_FIN,
            self.VL_BRT,
            ))
        return linha + super(RegistroC405, self).gerar_linha()


class RegistroC481(Registro):
    '''
    Resumo diário de documentos emitidos por ECF - PIS/PASEP (códigos 02 e 2D)
    '''

    def __init__(self):
        self.REG_PAI = "C405"
        self.REG = "C481"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_ITEM = ""
        self.COD_CTA = ""
        self.nivel = 5
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
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_ITEM,
            self.COD_CTA,
            ))
        return linha + super(RegistroC481, self).gerar_linha()


class RegistroC485(Registro):
    '''
    Resumo diário de documentos emitidos por ECF - Cofins (códigos 02 e 2D)
    '''

    def __init__(self):
        self.REG_PAI = "C405"
        self.REG = "C485"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_ITEM = ""
        self.COD_CTA = ""
        self.nivel = 5
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
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_ITEM,
            self.COD_CTA,
            ))
        return linha + super(RegistroC485, self).gerar_linha()


class RegistroC489(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C400"
        self.REG = "C489"
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
        return linha + super(RegistroC489, self).gerar_linha()


class RegistroC490(Registro):
    '''Consolidação de documentos emitidos por ECF (códigos 02, 2D e 59)'''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C490"
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.COD_MOD = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.COD_MOD,
            ))
        return linha + super(RegistroC490, self).gerar_linha()


class RegistroC491(Registro):
    '''
    Detalhamento da consolidação de documentos emitidos por ECF (códigos 02, 2D
    e 59) - PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "C490"
        self.REG = "C491"
        self.COD_ITEM = ""
        self.CST_PIS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.CST_PIS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC491, self).gerar_linha()


class RegistroC495(Registro):
    '''
    Detalhamento da consolidação de documentos emitidos por ECF (códigos 02, 2D
    e 59) - Cofins
    '''

    def __init__(self):
        self.REG_PAI = "C490"
        self.REG = "C495"
        self.COD_ITEM = ""
        self.CST_COFINS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.CST_COFINS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC495, self).gerar_linha()


class RegistroC499(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C490"
        self.REG = "C499"
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
        return linha + super(RegistroC499, self).gerar_linha()


class RegistroC500(Registro):
    '''
    Nota fiscal/conta de energia elétrica (código 06), nota fiscal/conta de
    fornecimento d'agua canalizada (código 29) e nota fiscal consumo
    fornecimento de gás (código 28) - documentos de entrada/aquisição com
    crédito.
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C500"
        self.COD_PART = ""
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.DT_DOC = ""
        self.DT_ENT = ""
        self.VL_DOC = ""
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
            self.COD_PART,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.DT_DOC,
            self.DT_ENT,
            self.VL_DOC,
            self.VL_ICMS,
            self.COD_INF,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroC500, self).gerar_linha()


class RegistroC501(Registro):
    '''Complemento da operacao (códigos 06, 28 e 29) - PIS/PASEP'''

    def __init__(self):
        self.REG_PAI = "C500"
        self.REG = "C501"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC501, self).gerar_linha()


class RegistroC505(Registro):
    '''Complemento da operacao (códigos 06, 28 e 29) - Cofins'''

    def __init__(self):
        self.REG_PAI = "C500"
        self.REG = "C505"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC505, self).gerar_linha()


class RegistroC509(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C500"
        self.REG = "C509"
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
        return linha + super(RegistroC509, self).gerar_linha()


class RegistroC600(Registro):
    '''
    Consolidação diária de notas fiscais/contas emitidas de energia elétrica
    (código 06), nota fiscal/conta de fornecimento d'água canalizada (código
    29) e nota fiscal/conta de fornecimento de gás (código 28) (empresas
    obrigadas ou não ao CONVÊNIO ICMS 115/03) - documentos de saída.
    '''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C600"
        self.COD_MOD = ""
        self.COD_MUN = ""
        self.SER = ""
        self.SUB = ""
        self.COD_CONS = ""
        self.QTD_CONS = ""
        self.QTD_CANC = ""
        self.DT_DOC = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.CONS = ""
        self.VL_FORN = ""
        self.VL_SERV_NT = ""
        self.VL_TERC = ""
        self.VL_DA = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.VL_BC_ICMS_ST = ""
        self.VL_ICMS_ST = ""
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
            self.COD_CONS,
            self.QTD_CONS,
            self.QTD_CANC,
            self.DT_DOC,
            self.VL_DOC,
            self.VL_DESC,
            self.CONS,
            self.VL_FORN,
            self.VL_SERV_NT,
            self.VL_TERC,
            self.VL_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_BC_ICMS_ST,
            self.VL_ICMS_ST,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroC600, self).gerar_linha()


class RegistroC601(Registro):
    '''
    Complemento da consolidação diária (códigos 06, 28 e 29) - documentos de
    saídas PIS/PASEP
    '''

    def __init__(self):
        self.REG_PAI = "C600"
        self.REG = "C601"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC601, self).gerar_linha()


class RegistroC605(Registro):
    '''
    Complemento da consolidação diária (códigos 06, 28 e 29) - documentos de
    saídas Cofins
    '''

    def __init__(self):
        self.REG_PAI = "C600"
        self.REG = "C605"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC605, self).gerar_linha()


class RegistroC609(Registro):
    '''Processo referenciado'''

    def __init__(self):
        self.REG_PAI = "C600"
        self.REG = "C609"
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
        return linha + super(RegistroC609, self).gerar_linha()


class RegistroC800(Registro):
    '''Cupom Fiscal Eletrônico (Código 59)'''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C800"
        self.COD_MOD = ''
        self.COD_SIT = ''
        self.NUM_CFE = ''
        self.DT_DOC = ''
        self.VL_CFE = ''
        self.VL_PIS = ''
        self.VL_COFINS = ''
        self.CNPJ_CPF = ''
        self.NR_SAT = ''
        self.CHV_CFE = ''
        self.VL_DESC = ''
        self.VL_MERC = ''
        self.VL_OUT_DA = ''
        self.VL_ICMS = ''
        self.VL_PIS_ST = ''
        self.VL_COFINS_ST = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_SIT,
            self.NUM_CFE,
            self.DT_DOC,
            self.VL_CFE,
            self.VL_PIS,
            self.VL_COFINS,
            self.CNPJ_CPF,
            self.NR_SAT,
            self.CHV_CFE,
            self.VL_DESC,
            self.VL_MERC,
            self.VL_OUT_DA,
            self.VL_ICMS,
            self.VL_PIS_ST,
            self.VL_COFINS_ST,
            ))
        return linha + super(RegistroC800, self).gerar_linha()


class RegistroC810(Registro):
    '''
    Detalhamento do Cupom Fiscal Eletrônico (Código 59) - PIS/PASEP e  COFINS
    '''

    def __init__(self):
        self.REG_PAI = "C800"
        self.REG = "C810"
        self.CFOP = ''
        self.VL_ITEM = ''
        self.COD_ITEM = ''
        self.CST_PIS = ''
        self.VL_BC_PIS = ''
        self.ALIQ_PIS = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.VL_BC_COFINS = ''
        self.ALIQ_COFINS = ''
        self.VL_COFINS = ''
        self.COD_CTA = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CFOP,
            self.VL_ITEM,
            self.COD_ITEM,
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
        return linha + super(RegistroC810, self).gerar_linha()


class RegistroC820(Registro):
    '''
    Detalhamento do Cupom Fiscal Eletrônico (código 59) - PIS/PASEP e COFINS
    Apurado por Unidade de Medida de Produto
    '''

    def __init__(self):
        self.REG_PAI = "C800"
        self.REG = "C820"
        self.CFOP = ''
        self.VL_ITEM = ''
        self.COD_ITEM = ''
        self.CST_PIS = ''
        self.QUANT_BC_PIS = ''
        self.ALIQ_PIS_QUANT = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.QUANT_BC_COFINS = ''
        self.ALIQ_COFINS_QUANT = ''
        self.VL_COFINS = ''
        self.COD_CTA = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se não existir C810
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CFOP,
            self.VL_ITEM,
            self.COD_ITEM,
            self.CST_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.CST_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC820, self).gerar_linha()


class RegistroC830(Registro):
    '''Processo Referenciado'''

    def __init__(self):
        self.REG_PAI = "C800"
        self.REG = "C830"
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
        return linha + super(RegistroC830, self).gerar_linha()


class RegistroC860(Registro):
    '''Identificação do Equipamento SAT - CF-e'''

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C860"
        self.COD_MOD = ''
        self.NR_SAT = ''
        self.DT_DOC = ''
        self.DOC_INI = ''
        self.DOC_FIM = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.NR_SAT,
            self.DT_DOC,
            self.DOC_INI,
            self.DOC_FIM,
            ))
        return linha + super(RegistroC860, self).gerar_linha()


class RegistroC870(Registro):
    '''
    Detalhamento do Cupom Fiscal Eletrônico (Código 59) - PIS/PASEP e COFINS
    '''

    def __init__(self):
        self.REG_PAI = "C860"
        self.REG = "C870"
        self.CFOP = ''
        self.VL_ITEM = ''
        self.COD_ITEM = ''
        self.CST_PIS = ''
        self.VL_BC_PIS = ''
        self.ALIQ_PIS = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.VL_BC_COFINS = ''
        self.ALIQ_COFINS = ''
        self.VL_COFINS = ''
        self.COD_CTA = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CFOP,
            self.VL_ITEM,
            self.COD_ITEM,
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
        return linha + super(RegistroC870, self).gerar_linha()


class RegistroC880(Registro):
    '''
    Detalhamento do Cupom Fiscal Eletrônico (Código 59) - PIS/PASEP e COFINS
    Apurado por Unidade de Medida de Produto
    '''

    def __init__(self):
        self.REG_PAI = "C860"
        self.REG = "C880"
        self.COD_ITEM = ''
        self.CFOP = ''
        self.VL_ITEM = ''
        self.CST_PIS = ''
        self.QUANT_BC_PIS = ''
        self.ALIQ_PIS_QUANT = ''
        self.VL_PIS = ''
        self.CST_COFINS = ''
        self.QUANT_BC_COFINS = ''
        self.ALIQ_COFINS_QUANT = ''
        self.VL_COFINS = ''
        self.COD_CTA = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        # se não existir C870
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.CFOP,
            self.VL_ITEM,
            self.CST_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.CST_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC880, self).gerar_linha()


class RegistroC890(Registro):
    '''Processo Referenciado'''

    def __init__(self):
        self.REG_PAI = "C860"
        self.REG = "C890"
        self.NUM_PROC = ''
        self.IND_PROC = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            ))
        return linha + super(RegistroC890, self).gerar_linha()


class RegistroC990(RegistroX990):
    '''Encerramento do bloco C'''

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "C990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.QTD_LIN))
        return linha + super(RegistroC990, self).gerar_linha()
