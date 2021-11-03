import subprocess
import os, sys
from files import Filegetter


path = 'C:/STATYKA BIAŁYSTOK/Łomża/POMIAR/RINEX/15.10'
f = Filegetter(path)
a = f.get_list_of(with_sufix='.21O')
print(a)

f._21o2rnx(a[0])
print(os.listdir(path))
b = f.get_list_of(with_sufix='.rnx') 
print(b)
c = f._rnx2version2(b[0]) # doesn't work

  