from genericpath import isfile
from files import Filegetter
import os.path

if __name__ == '__main__':
    path = 'C:/STATYKA GLIWICE/Marklowice/2/POMIAR/próba nr 2/Stat 5.11.21'
    if os.path.isfile(path):
        pass
    else:
        path = input("Put the path here : ->")

    file_getter = Filegetter(path)
    file_getter.run()
