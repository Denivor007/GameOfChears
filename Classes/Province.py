from Classes.State import *
from Classes.Buildings import *

levels = {
    1:5,
    2:7,
    3:10,
    4:12,
    5:15
}

'''класс строения должен иметь цену, стоимость обслуживания (по дефолту 5% от цены)
а так-же характеристики, т.е. что он позволяет делать


'''



class Province:
    def __init__(self,
                 state = State,
                 level = int,
                 array_of_buildings = list,
                 popularity = int,
                 trained_units = int,
                 hunger = int):
        self.state = state
        self.level = level #пока взаимодействие не реализовано
        self.array_of_buildings = list(array_of_buildings)
        self.popularity = popularity #пока взаимодействие не реализовано


    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, lvl):
        lvls = levels.keys()
        if lvl not in lvls:
            raise Exception("{}incorrect level of province, should be between {} and {}".format(lvl, min(lvls), max(lvls)))
        self._level = lvl


    def changeState(self, state):
        #if type(state) != type(State):
        #   raise Exception("{} is not {}\n{} is not State object".format(type(state),type(State),state))
        if self in self.state.array_of_provinces:
            self.state.array_of_provinces.remove(self)
        self.state = state

    def buildSomething(self, building):
        if type(building) != type(Building):
            raise Exception("Not a building")
        if len(self.array_of_buildings) >= levels[self.level]:
            raise Exception("Maximum count of buildings")
        if building.price > self.state.resourses:
            raise Exception("Out Of Rerourses")
        self.array_of_buildings.add(building)
        self.state.resourses = self.state.resourses - building.price

    def __str__(self):
        res = "{}st level\n"
        res += "State: {}\n"
        res += "Builings: \n"
        for building in self.array_of_buildings:
            res += "\t--{}\n".format(str(building))
        res += "popularity: {}".format(self.popularity)
        return res.format(self.level, self.state.name)




