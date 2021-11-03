import os
import sys
import subprocess as s

class Filegetter:
    def __init__(self, path):
        self.path = path
        self.program = 'gfzrnx_1.15-8044_win64.exe'
    
    def get_list_of(self, with_sufix = '.21o'):
        names = []
        for i in os.listdir(self.path):
            if with_sufix.lower() in i:
                names.append(i)
        return names

    def _21o2rnx(self, name, sats= 'GREC'):

        '''
        sats must be a continuous string of characters of expecting satelities 
        and could be: G - GPS, R - GLONASS, E - BeiDou, 
        S - SBAS, J - QZSS, I - IRNSS 
        '''
        s.call([self.program, '-finp', name, '-fout', '::RX3::POL,00', '-satsys', sats.upper()], cwd = self.path)
    

    def _rnx2version2(self, name):
        s.call([self.program, '-finp', name, '-fout', '::RX2:: --version_out 2'], cwd = self.path) 
