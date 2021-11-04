import os, sys, subprocess
from files import Filegetter

if __name__ == '__main__':
    path = 'C:/STATYKA BIAŁYSTOK/Łomża/POMIAR/RINEX/15.10'
    f = Filegetter(path)
    f.copyf(path)
    a = f.get_list_of(with_sufix='.21O')
    f._21o2rnx(a[0])
    b = f.get_list_of(with_sufix='.rnx') 
    c = f._rnx2version2(b[0]) # doesn't work
