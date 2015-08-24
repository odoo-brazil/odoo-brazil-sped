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

from util import Ocorrencia


class Registro(object):
    '''Registro do layout EFD PIS/COFINS.'''

    registros9900 = {}

    def __init__(self):
        # Indica o nome do registro pai.
        self.REG_PAI = None
        self.nivel = 0
        self.REG = "0000"
        self.registros_filhos = []

    @staticmethod
    def get_registro9001_static():
        return Registro.registro9001

    def get_bloco(self):
        bloco = ""

        if len(self.REG) > 0:
            bloco = self.REG[:1]

        return bloco

    def preencher_valores_dos_campos_pela_linha(self, linha):
        raise NotImplementedError("Deveria ter implementado isso")

    def gerar_linha_de_registros(self, registros):
        return u'|%s\r\n' % ((u'%s|' * len(registros)) % registros)

    def gerar_linha(self):
        sb = ''
        for registro in self.registros_filhos:
            sb += registro.gerar_linha()
        return sb

    def add_registro_filho(self, registro):
        if registro is None or self.REG != registro.REG_PAI:
            raise Exception("Registro filho inválido!")

        if registro in self.registros_filhos:
            return

        if registro.__class__.__name__ == 'Registro9900':
            raise Exception(
                      "Nao e permitido adicionar o registro 9900 !\n"
                    + "Esse registro e criado e adicionado automaticamente "
                    + "conforme outros registros vao sendo adicionados !")

        self.add_registro_filho_interno(registro)

    def add_registro_filho_interno(self, registro):
        from RegistroX990 import RegistroX990
        if isinstance(self, RegistroX001) and \
            not isinstance(registro, (RegistroX001, RegistroX990)):
            self.IND_MOV = "0"

        self.registros_filhos.append(registro)
        self.criar_ou_obter_registro9900_e_atualizar_QTD_REG_BLC(registro)

    def get_quantidade_total_de_registros(self):
        total_de_registros = 1
        for registro in self.registros_filhos:
            total_de_registros += registro.get_quantidade_total_de_registros()
        return total_de_registros

    def criar_ou_obter_registro9900_e_atualizar_QTD_REG_BLC(self, registro):
        reg9900 = Registro.registros9900.get(registro.REG)

        if reg9900 is None:
            from bloco9 import Registro9900
            reg9900 = Registro9900(registro.REG)
            Registro.registros9900[registro.REG] = reg9900
            Registro.registro9001.add_registro_filho_interno(reg9900)

        reg9900.incrementar_QTD_REG_BLC()

    def fix_linha(self, linha):
        if linha.startswith("|0"):
            linha = "0" + linha
        if linha.startswith("|A"):
            linha = "1" + linha
        if linha.startswith("|C"):
            linha = "2" + linha
        if linha.startswith("|D"):
            linha = "3" + linha
        if linha.startswith("|F"):
            linha = "4" + linha
        if linha.startswith("|M"):
            linha = "5" + linha
        if linha.startswith("|P"):
            linha = "6" + linha
        if linha.startswith("|1"):
            linha = "7" + linha
        if linha.startswith("|9"):
            linha = "8" + linha
        return linha

    def __eq__(self, o):
        return self.fix_linha(self.gerar_linha()) == \
            self.fix_linha(o.gerar_linha())

    def __lt__(self, o):
        return self.fix_linha(self.gerar_linha()) < \
            self.fix_linha(o.gerar_linha())

    def __gt__(self, o):
        return self.fix_linha(self.gerar_linha()) > \
            self.fix_linha(o.gerar_linha())

    def __le__(self, o):
        return self.fix_linha(self.gerar_linha()) <= \
            self.fix_linha(o.gerar_linha())

    def __ge__(self, o):
        return self.fix_linha(self.gerar_linha()) >= \
            self.fix_linha(o.gerar_linha())

    def __ne__(self, o):
        return self.fix_linha(self.gerar_linha()) != \
            self.fix_linha(o.gerar_linha())


class RegistroX001(Registro):
    '''Classe para Registros X001 do layout EFD-PIS/COFINS. Representa a
    abertura do bloco X, sendo X igual a 0, A, C, D, F, M, P, 1 ou 9.
    '''

    def __init__(self):
        '''
        Indicador de movimento:
        0 - Bloco com dados informados.
        1 - Bloco sem dados informados.
        '''
        self.IND_MOV = "1"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM

    def gerar_linha(self):
        self.registros_filhos.sort()
        return super(RegistroX001, self).gerar_linha()
