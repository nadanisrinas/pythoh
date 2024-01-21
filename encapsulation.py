from abc import abstractmethod


class Warga: 
    def __init__(self, NIK: str, name: str): 
        self.NIK = NIK 
        self.__name = name

    def get_name(self):
        return self.__name 
    
    def set_name(self,name):
        self.__name = name


mukhlis.set_name("nada")

print(mukhlis.get_name())