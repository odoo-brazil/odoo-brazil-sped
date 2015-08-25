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

import abc, base64
from datetime import datetime


class SpedBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.execution_id = 0

    def _create_new_execution(self, cr, uid, ids=None,
                              context=None, obligation=None):
        pool_execution = obligation.pool.get('fiscal.obligation.execution')
        new_obj = {'code': 1, 'date_execution_start': datetime.now(),
                   'date_execution_end': datetime.now(), 'running': True,
                   'fiscal_obligation_id': obligation.id}
        generated_id = pool_execution.create(cr, uid, new_obj, context)
        self.execution_id = generated_id
        return generated_id

    def _set_as_generated(self, cr, uid, ids=None, context=None,
                          obligation=None, content=None):
        pool_obligation = obligation.pool.get('fiscal.obligation')
        pool_execution = obligation.pool.get('fiscal.obligation.execution')
        pool_obligation.write(cr, uid, ids, {'generate': False, }, context)

        print type(content)
        if not content is None:
            print content.encode('utf-8')
            result = base64.b64encode(content.encode('utf-8'))
            pool_execution.write(cr, uid, self.execution_id,
                                 {'date_execution_end': datetime.now(),
                                  'running': False, 'efd_fiscal_file': result},
                                 context)
        else:
            pool_execution.write(
                cr, uid, self.execution_id, {
                    'date_execution_end': datetime.now(), 'running': False},
                context)

    def _create_new_message(self, cr, uid, ids=None, context=None,
                            obligation=None, execution_id=None, message=None):
        pool_message = obligation.pool.get('fiscal.obligation.messages')
        pool_message.create(cr, uid,
                            {'message': message,
                             'fiscal_obligation_execution_id': execution_id},
                            context)
        
    @abc.abstractmethod
    def generate(self, cr, uid, ids=None, context=None, obligation=None):
        return 
