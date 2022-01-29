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
GLOBAL = State("GLOBAL")
provs= [
 Province(GLOBAL, 1, [Kazarma, Farm], 90),
 Province(GLOBAL, 1, [Kazarma, Farm], 80),
 Province(GLOBAL, 1, [Kazarma, Farm], 90),
 Province(GLOBAL, 1, [Kazarma, Farm], 80),
 Province(GLOBAL, 1, [Kazarma, Farm], 90),
 Province(GLOBAL, 1, [Kazarma, Farm], 80)
]

my_state = State
def main():
    while True:
        name = input("Выбери имя страны")
        if 1 < len(name) < 32:
            my_state.name = name
            break
    while True:
        message = "Выбери команду"
        message += "\n1-Захватить провинцию \n2-Мои провинции \n3-Все провинции"
        print("Выбери команду")
        if message == 1:
            pass






