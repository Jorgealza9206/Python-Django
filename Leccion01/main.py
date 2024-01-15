import random

# Define los equipos en cada bombo
bombo1 = ["Uzbekistán", "Irán", "Corea del Sur", "Japón"]
bombo2 = ["Australia", "Emiratos Árabes Unidos", "China", "Irak"]
bombo3 = ["Malasia", "Tailandia", "Vietnam", "Siria"]
bombo4 = ["Jordania", "Qatar", "Tayikistán", "Indonesia"]

# Define los grupos
grupos = {}
for i in range(1, 5):
    grupos[f"Grupo {chr(64+i)}"] = []

print(grupos)

#Realizamos el sorteo del primer bombo
equipo1 = bombo1[0]
grupos[f"Grupo {chr(65)}"].append(equipo1)
bombo1.remove(equipo1)
equipo2 = random.choice(bombo1)
grupos[f"Grupo {chr(66)}"].append(equipo2)
bombo1.remove(equipo2)
equipo3 = random.choice(bombo1)
grupos[f"Grupo {chr(67)}"].append(equipo3)
bombo1.remove(equipo3)
equipo4 = random.choice(bombo1)
grupos[f"Grupo {chr(68)}"].append(equipo4)
bombo1.remove(equipo4)
print(grupos)
