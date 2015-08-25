'''
Created on 24 de ago de 2015

@author: danimar
'''

from ..sped_base import SpedBase


class BlocoI(SpedBase):

    def generate(self, cr, uid, ids=None, context=None, 
                 obligation=None, arquivo_digital=None):
        return 