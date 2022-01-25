from Classes.Province import *
class State:
    def __init__(self, _name_ ):
        self.name = _name_
        self.arrayOfProvinces = []
        self.popularityModifier = 0
        self.resourses = Resourses

    def append(self, prov ):
        prov.changeState(self)
        self.arrayOfProvinces.append(prov)

    def printState(self):
        res = "|---\""+self.name+"\"---|"
        res += str(self.resourses)
        for prov in self.arrayOfProvinces:
            res += str(prov)
        return res
    def getProvArray(self):
        return

    def __str__(self):
        res = "|---\"" + self.name + "\"---|"
        res += "{}\n".format(str(self.resourses))
        i = 0
        for prov in self.arrayOfProvinces:
            i += 1
            res += "prov{} {}\n".format(i,str(prov))
            res += "____\n"
        return res
