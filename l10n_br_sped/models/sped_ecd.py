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

#python-sped Python 3 - Não importa ArquivoDigital ainda
from sped.ecd.arquivos import ArquivoDigital
from .sped_base import SpedBase
from .ecd.bloco_0 import Bloco0
from .ecd.bloco_I import BlocoI
from .ecd.bloco_J import BlocoJ
from .ecd.bloco_9 import Bloco9


class SpedECD(SpedBase):

    def generate(self, cr, uid, ids=None, context=None, obligation=None):
        execution_id = self._create_new_execution(cr, uid, ids,
                                                  context, obligation)
        self._create_new_message(cr, uid, ids, context,
                                 obligation, execution_id,
                                 "Iniciado a gerar o arquivo ECD")


        arquivo_digital = ArquivoDigital()   

        bloco0 = Bloco0()
        bloco0.generate(cr, uid, ids, context, obligation, arquivo_digital)

        blocoI = BlocoI()
        blocoI.generate(cr, uid, ids, context, obligation, arquivo_digital)

        blocoj = BlocoJ()
        blocoj.generate(cr, uid, ids, context, obligation, arquivo_digital)

        bloco9 = Bloco9()
        bloco9.generate(cr, uid, ids, context, obligation, arquivo_digital)

        arquivo_digital.prepare()
        content = arquivo_digital.getstring()

        self._set_as_generated(cr, uid, ids, context, obligation, content)
        self._create_new_message(cr, uid, ids, context, obligation,
                                 execution_id, "Arquivo ECD finalizado")
        
        
