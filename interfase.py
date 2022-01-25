from Classes.Province import *
import tkinter as tk
dictOfBuildings = {
    "barracks" : Building("barracks",300, 200, 200, 20),
    "farm" : Building("farm",250, 300, 100, 20),

}

iven = State('ivenstolm')
prov1 = Province(iven, 1, [dictOfBuildings["barracks"], dictOfBuildings["farm"]], 90)
prov2 = Province(iven, 1, [dictOfBuildings["farm"], dictOfBuildings["barracks"]], 80)
iven.append(prov1)
iven.append(prov2)
prov = iven.arrayOfProvinces[0]

dictOfProv = {}
for i in range(len(iven.arrayOfProvinces)):
    dictOfProv[i] = iven.arrayOfProvinces[i]

def update():
    global prov
    state_inf.config(text = str(prov))
    for i in range(len(iven.arrayOfProvinces)):
        if int(list_of_prov.curselection)  == i:
            prov = i


def addBarraks(prov = Province):
    update()
    prov.buildSomething(dictOfBuildings["barracks"])

def addFarm(prov = Province):
    update()
    prov.buildSomething(dictOfBuildings["barracks"])

root = tk.Tk()
state_inf = tk.Label(width = 15, height = 10).pack()
add_barraks_button = tk.Button(text = "add barak",
                               width = 15,
                               height = 10,
                               command = lambda prov = prov: addBarraks(prov)).pack()
add_farm_button = tk.Button(text = "add farm",
                            width = 15,
                            height = 10,
                            command = lambda prov = prov: addBarraks(prov)).pack()

list_of_prov = tk.Listbox(width = 15, height = 10).pack()
for i in range(len(iven.arrayOfProvinces)):
    list_of_prov.insert(0, i)
root.bind('<Return>', update)
root.mainloop()






