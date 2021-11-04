import os
import sys
import subprocess
import shutil

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
        for i in name:
            subprocess.call([self.program, '-finp', i, '-fout', '::RX3::POL,00', '-satsys', sats.upper()], cwd = self.path)

    def _rnx2version2(self, name2):
        for i in name2:
            subprocess.call([self.program, '-finp', i, '-fout', '::RX2::POL,00', ' --version_out 2 '], cwd = self.path) 

    def copyf(self):
        try:
            shutil.copy(os.getcwd() + '/' + self.program, self.path)
            print('Copy file successfully')
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
        except IsADirectoryError:
            print("Destination is a directory.")
        except PermissionError:
            print("Permission denied.")
        except:
            print("Error occurred while copying file.")
    
    def run(self):
        self.copyf()
        a = self.get_list_of(with_sufix='.21O')
        self._21o2rnx(a)
        b = self.get_list_of(with_sufix='.rnx') 
        self._rnx2version2(b)
