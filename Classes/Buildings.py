from Imports import *
from abc import *


"""
потом, будем уверенны, нам придётся добавлять классы построек для разных уровней,
возможно паттерн: "абстрактная фабрика" нам поможет
"""


class Building(ABC):
    def __init__(self, name = str, strength = int, resourses = Resourses):
        self.name = name
        self.price = resourses
        self.strength = strength

    @abstractmethod
    def doSomething(self):
        pass

    @abstractmethod
    def __str__(self):
        return str(self.name)


class Farm(Building):
    def __init__(self, name=str, strength=int, resourses=Resourses):
        super.__init__("farm", strength ,Resourses(300,200,50) )

    def doSomething(self):
        print("i grow the farm")

    def __str__(self):
        return str(self.name)


class Kazarma(Building):
    def __init__(self, name=str, strength=int, resourses=Resourses):
        self.name = "kasarm"
        super.__init__("kasarm", strength ,Resourses(400,100,300) )

    def doSomething(self):
        print("im teach the army")

    def __str__(self):
        return str(self.name)