# -*- coding: utf-8 -*-

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

from registers import *
import itertools

class EFD:

    '''
    Default version: 1.05
    Other possible values:
    Code   Version Begin date  End date
    002    1.01    01012009    31122009
    003    1.02    01012010    31122010
    004    1.03    01012011    31122011
    005    1.04    01012012    30062012
    006    1.05    01072012    
    '''
    version = '006'

    registers = {
        '0': [],
        'C': [],
        'D': [],
        'E': [],
        'G': [],
        'H': [],
        '1': [],
        '9': [],
        }

    class RequiredException(Exception): pass

    def __init__(self, COD_FIN, DT_INI, DT_FIN, NOME, CNPJ, CPF, UF, IE,
                 COD_MUN, IM, SUFRAMA, IND_PERFIL, IND_ATIV):
        """EFD constructor.

        Parameters
        ----------
        COD_FIN : number
            Código da finalidade do arquivo:
            0 - Remessa do arquivo original;
            1 - Remessa do arquivo substituto.
        DT_INI : number
            Data inicial das informações contidas no arquivo.
        DT_FIN : number
            Data final das informações contidas no arquivo.
        NOME : string
            Nome empresarial da entidade.
        CNPJ : number
            Número de inscrição da entidade no CNPJ.
        CPF : number
            Número de inscrição da entidade no CPF.
        UF : string
            Sigla da unidade da federação da entidade.
        IE : string
            Inscrição Estadual da entidade.
        COD_MUN : number
            Código do município do domicílio fiscal da entidade, conforme a
            tabela IBGE.
        IM : string
            Inscrição Municipal da entidade.
        SUFRAMA : string
            Inscrição da entidade na SUFRAMA.
        IND_PERFIL : string
            Perfil de apresentação do arquivo fiscal;
            A - Perfil A;
            B - Perfil B;
            C - Perfil C.
        IND_ATIV : number
            Indicador de tipo de atividade:
            0 - Industrial ou equiparado a industrial;
            1 - Outros.
        """
        self.registers['0'].append(r0000(
            self.version,
            COD_FIN,
            DT_INI,
            DT_FIN,
            NOME,
            CNPJ,
            CPF,
            UF,
            IE,
            COD_MUN,
            IM,
            SUFRAMA,
            IND_PERFIL,
            IND_ATIV
            ))

    def add(self, reg):
        self.registers[reg.block].append(reg)
    
    def _validate(self):
        registers = list(itertools.chain.from_iterable(
            [self.registers[block] for block in self.registers]
            ))
        register_ids = set([r.REG for r in registers])

        required_registers = (
            '0000', '0001', '0005', '0990',
            'C001', 'C990',
            'D001', 'D990',
            'E001', 'E100', 'E110', 'E990',
            'G001', 'G990',
            'H001', 'H990',
            '1001', '1010', '1990',
            '9001', '9900', '9990', '9999',
            )
        for reg in required_registers:
            if reg not in register_ids:
                raise EFD.RequiredException(
                    u'O registro {} deve ser informado.'.format(reg)
                    )

    def _generate_end_blocks(self):
        '''Generate end blocks' data'''

        # Count all registers 
        total_len = 0

        # Count each register type
        reg_len = {}

        for block in self.registers:
            block_len = len(self.registers[block])

            reg_begin, reg_end = None, None

            # Don't count the register 0000, created by default 
            if block == '0':
                ind_mov = block_len > 1 and '0' or '1'
            else:
                ind_mov = block_len and '0' or '1'

            # Sum the registers that will be added
            block_len += 2

            # Create register for beginning and end of the current block
            if block == '0':
                reg_begin = r0001(IND_MOV=ind_mov)
                reg_end = r0990(QTD_LIN_0=block_len)
            elif block == 'C':
                reg_begin = rC001(IND_MOV=ind_mov)
                reg_end = rC990(QTD_LIN_C=block_len)
            elif block == 'D':
                reg_begin = rD001(IND_MOV=ind_mov)
                reg_end = rD990(QTD_LIN_D=block_len)
            elif block == 'E':
                reg_begin = rE001(IND_MOV=ind_mov)
                reg_end = rE990(QTD_LIN_E=block_len)
            elif block == 'G':
                reg_begin = rG001(IND_MOV=ind_mov)
                reg_end = rG990(QTD_LIN_G=block_len)
            elif block == 'H':
                reg_begin = rH001(IND_MOV=ind_mov)
                reg_end = rH990(QTD_LIN_H=block_len)
            elif block == '1':
                reg_begin = r1001(IND_MOV=ind_mov)
                reg_end = r1990(QTD_LIN_1=block_len)

            if reg_begin and reg_end:
                self.registers[block].append(reg_begin)
                self.registers[block].append(reg_end)

            # Sum one for each register type
            for register in self.registers[block]:
                try:
                    reg_len[register.REG] += 1
                except:
                    reg_len[register.REG] = 1

        # Sum the count of each block
        for block in self.registers:
            block_len = len(self.registers[block])
            total_len += block_len

        if total_len != 0:
            self.registers['9'].append(r9001(IND_MOV=0))
        else:
            self.registers['9'].append(r9001(IND_MOV=1))
        reg_len['9001'] = 1
        total_len += 1

        # Starts with 2: 9990 and 9999
        reg_len['9900'] = 2
        for reg in reg_len:
            reg_len['9900'] += 1

        reg_len['9990'] = 1
        reg_len['9999'] = 1

        for reg in reg_len:
            self.registers['9'].append(r9900(
                REG_BLC=reg,
                QTD_REG_BLC=reg_len[reg],
                ))
            total_len += 1

        # Sum registers 9990 and 9999
        self.registers['9'].append(r9990(
            QTD_LIN_9=len(self.registers['9']) + 2
            ))

        # Again, sum registers 9990 and 9999
        total_len += 2
        self.registers['9'].append(r9999(QTD_LIN=total_len))
    
    def _unicode(self, value):
        if isinstance(value, unicode):
            return value
        val = str(value)
        return val.decode('utf-8', 'ignore')

    def generate(self):
        '''Generate EFD file content'''
        self._generate_end_blocks()
        try:
            self._validate()
        except EFD.RequiredException, e:
            print(e.message)

        lines = []

        for block in self.registers:
            for reg in self.registers[block]:
                reg_dict = reg.attrs
                line = u'|'.join(map(self._unicode,
                    [reg.__getattribute__(key) for key in reg_dict]
                    ))
                lines.append(u'|{}|{}|'.format(reg.REG, line))
 
        def _fix_key(key):
            if key.startswith('0'):
                key = '0' + key
            elif key.startswith('C'):
                key = '1' + key
            elif key.startswith('D'):
                key = '2' + key
            elif key.startswith('E'):
                key = '3' + key
            elif key.startswith('G'):
                key = '4' + key
            elif key.startswith('H'):
                key = '5' + key
            elif key.startswith('1'):
                key = '6' + key
            elif key.startswith('9'):
                key = '7' + key
            return key
 
        def _get_line_key(line):
            key = _fix_key(line[1:5])
            if line[1:5] == '9900':
                key = key + _fix_key(line[6:10])
            return key

        lines = sorted(lines, key=_get_line_key)

        return '\r\n'.join(lines)
