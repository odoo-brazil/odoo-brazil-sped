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
from Registro import Registro


class RegistroX990(Registro):
    '''
    Classe para Registros X990 do layout EFD-PIS/COFINS. Representa o
    encerramento do bloco X, sendo X igual a 0, A, C, D, F, M, P, 1 ou 9.
    '''

    def __init__(self):
        self.QTD_LIN = '0'
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.registros_filhos = []
