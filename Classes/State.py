from Classes.Resourses import *
from Classes.Province import *

class State:
    def __init__(self, _name_):
        self.name = _name_
        self.array_of_provinces = []
        self.popularityModifier = 0
        self.resourses = Resourses()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nm = str):
        self._name = nm

    def append(self, prov ):
        prov.changeState(self)
        self.array_of_provinces.append(prov)

    def printState(self):
        res = "|---\""+self.name+"\"---|"
        res += str(self.resourses)
        for prov in self.array_of_provinces:
            res += str(prov)
        return res
    def getProvArray(self):
        return

    def __str__(self):
        res = "|---\"" + self.name + "\"---|"
        res += "{}\n".format(str(self.resourses))
        i = 0
        for prov in self.array_of_provinces:
            i += 1
            res += "prov{} {}\n".format(i,str(prov))
            res += "____\n"
        return res
