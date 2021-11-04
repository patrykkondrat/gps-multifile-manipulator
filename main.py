import os, sys, subprocess
from files import Filegetter

if __name__ == '__main__':
    path = 'C:/STATYKA BIAŁYSTOK/Łomża/POMIAR/RINEX/15.10'
    f = Filegetter(path)
    f.run()
