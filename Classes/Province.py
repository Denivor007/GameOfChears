from Classes.Resourses import *

levels = {
    1:5,
    2:7,
    3:10,
    4:12,
    5:15
}

'''класс строения должен иметь цену, стоимость обслуживания (по дефолту 5% от цены)
а так-же характеристики, т.е. что он позволяет делать'''
class Building:
    def __init__(self, name = "building", money = 1000, wood = 200, stone = 200, iron = 50):
        self.name = name
        self.price = Resourses(money,wood,stone,iron)

    def __str__(self):
        return str(self.name)

class State(object):
    pass
class Province:
    def __init__(self,state = State, level = int, arrayOfBuildings = set, popularity = int):
        self.state = state
        self.level = level
        self.arrayOfBuildings = set(arrayOfBuildings)
        self.popularity = popularity

    def changeState(self, state_ = State):
        if self in self.state.arrayOfProvinces:
            self.state.arrayOfProvinces.remove(self)
        self.state = state_

    def buildSomething(self, building = Building):
        if len(self.arrayOfBuildings) >= levels[self.level]:
            raise Exception("Maximum count of buildings")
        if building.price > self.state.resourses:
            raise Exception("Out Of Rerourses")
        self.arrayOfBuildings.add(building)
        self.state.resourses = self.state.resourses - building.price

    def __str__(self):
        res = "{}st level\n"
        res += "State: {}\n"
        res += "Builings: \n"
        for building in self.arrayOfBuildings:
            res += "\t--{}\n".format(str(building))
        res += "popularity: {}".format(self.popularity)
        return res.format(self.level, self.state.name)




