from Imports import *
from Classes.State import State

'''
Реализовать:
    - покупку постройки
    - продумать действия построек
    
Идеи:
    1. можно добавить в провинцию свойства по типу: потребление пищи,
       возможность призыва войск, призыва флота. А в постройках
       добавлять модификаторы этих характеристик
'''

iven = State("iven")
prov1 = Province(iven, 1, [Kazarma, Farm], 90)
prov2 = Province(iven, 1, [Kazarma, Farm], 80)
iven.append(prov1)
iven.append(prov2)
print(iven)
Kazarma.doSomething((iven.array_of_provinces[0].array_of_buildings[0]))