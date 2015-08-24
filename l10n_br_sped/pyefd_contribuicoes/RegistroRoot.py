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

from Registro import Registro
from bloco0 import Registro0000
from bloco9 import Registro9999
from util import Obrigatoriedade


class RegistroRoot(Registro):
    '''
    Registro root e o registro inicial em que são armazedos os registros
    iniciais de nível 0, ou seja, os registros 0000 e 9999.

    Para o programador é o ponto de partida e através deste objeto é possível
    adicionar os demais registros e gerar o arquivo EFD-PIS/Cofins.

    Exemplo:

    rr = RegistroRoot()
    r0100 = Registro0100()
    rr.registro0000.registro0001.add_registro_filho(r0100)
    rr.gerar("~/arquivo.txt")
    '''

    registro0000 = Registro0000()
    registro9999 = Registro9999()

    def __init__(self):
        self.REG = "ROOT"
        self.REG_PAI = None
        self.nivel = -1
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []
        super(RegistroRoot, self).add_registro_filho(self.registro0000)
        super(RegistroRoot, self).add_registro_filho(self.registro9999)

    def gerar(self, caminho):
        self.registro0000.atualizar_qtde_registros_de_encerramento_de_bloco()
        # Atualiza quantidade total de registros
        self.registro9999.QTD_LIN = str(
                                    self.get_quantidade_total_de_registros())

        f = open(caminho, 'w')
        f.write(self.gerar_linha())
        f.close()

    def add_registro_filho(self, registro):
        raise Exception(
                  "Nao e possivel adicionar registros filhos "
                + "no registro root ! \nAo inves disso, utilize conforme "
                + "exemplo abaixo: \n\n"
                + "RegistroRoot rr = new RegistroRoot() \n"
                + "Registro0100 r0100 = new Registro0100() \n"
                + "rr.getRegistro0000().getRegistro0001()"
                + ".add_registro_filho(r0100) \n")

    def get_quantidade_total_de_registros(self):
        # Retorna menos um pois este registro root nao conta
        qtde = super(RegistroRoot, self).get_quantidade_total_de_registros()
        return qtde - 1
