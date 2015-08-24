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


class Registro9001(RegistroX001):
    '''Abertura do bloco 9'''

    def __init__(self):
        super(Registro9001, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "9001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(Registro9001, self).gerar_linha()

Registro.registro9001 = Registro9001()


class Registro9900(Registro):
    '''Registros do arquivo'''

    def __init__(self, REG_BLC='XXXX'):
        self.REG_PAI = "9001"
        self.REG = "9900"
        self.REG_BLC = REG_BLC
        self.QTD_REG_BLC = "0"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def incrementar_QTD_REG_BLC(self):
        quantidade = int(self.QTD_REG_BLC) + 1
        self.QTD_REG_BLC = str(quantidade)

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.REG_BLC,
            self.QTD_REG_BLC,
            ))
        return linha + super(Registro9900, self).gerar_linha()


class Registro9990(RegistroX990):
    '''Encerramento do bloco 9'''

    def __init__(self):
        super(Registro9990, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "9990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(Registro9990, self).gerar_linha()


class Registro9999(Registro):
    '''Encerramento do arquivo digital'''

    def __init__(self):
        self.REG_PAI = "ROOT"
        self.REG = "9999"
        self.nivel = 0
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

        # Quantidade total de linhas do arquivo digital.
        self.QTD_LIN = "49"

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(Registro9999, self).gerar_linha()
