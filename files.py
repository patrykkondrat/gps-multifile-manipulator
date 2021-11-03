import os
import sys

class Filegetter:
    def __init__(self, path):
        self.path = path

    def list_of_21o(self, without_sufix=['.21o']):
        names = []
        for i in os.listdir(self.path):
            if i in without_sufix:
                names.append(i)
        return names
    
    def list_of_rnx(self):
        