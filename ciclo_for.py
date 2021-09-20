# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:49:09 2021

@author: Andres Vasquez
"""

# Punto #1------------------------------------------------------------------

menu = 1
color = 1
colores = [0, 0, 0, 0, 0]
all_placas = []
lista_placas = {}


def verificar(num_placa):
    last_number = int(num_placa[-1])
    print(f"Verificar: {last_number}")
    if last_number == 1 or last_number == 2:
        pos = 0
        colores[pos] += color
        lista_placas['Amarillo'] = colores[pos]
    elif last_number == 3 or last_number == 4:
        pos = 1
        colores[pos] += color
        lista_placas['Rosa'] = colores[pos]
    elif last_number == 5 or last_number == 6:
        pos = 2
        colores[pos] += color
        lista_placas['Roja'] = colores[pos]
    elif last_number == 7 or last_number == 8:
        pos = 3
        colores[pos] += color
        lista_placas['Verde'] = colores[pos]
    else:
        pos = 4
        colores[pos] += color
        lista_placas['Azul'] = colores[pos]


def verPlaca():
    print("\nPlacas registradas\n"
          "--------------------------------------\n")
    for valor in all_placas:
        print(f"{valor}\n")


def verColores():
    print("Colores de autos\n"
          "---------------------------------------\n")
    for nombre, valor in lista_placas.items():
        print(f"\n{nombre}: {valor}")


while menu != 4:
    if (menu == 1):
        num_placa = input("\nDigite el numero de placa: ")
        all_placas.append(num_placa)
        verificar(num_placa)
    elif (menu == 2):
        verColores()
    elif(menu == 3):
        verPlaca()
    else:
        print("\nDigito un numero erroneo")
    menu = int(input("\nMENU\n"
                     "-------------------------------------------\n"
                     "1. Digitar placa\n"
                     "2. Ver colores de autos\n"
                     "3. Ver placas registradas\n"
                     "4. Salir\n"
                     "Digita la opcion: "))
verColores()
print("\n-------------------------------------------\n"
      "Gracias por usar nuestro software")

# Punto #2 ------------------------------------------------------------------

menu = 1
lista_animales = []
lista_porcentaje = [0, 0, 0]


def edadElefante(valor, animal):
    edad = 0
    for pos in range(1):
        lista_animales.append([])
        for pos2 in range(valor):
            edad = int(input(f'Cuantos años tiene el Elefante #{pos2+1}: '))
            lista_animales[pos].append(edad)
    print(lista_animales)


def edadJirafa(valor, animal):
    edad = 0
    for pos in range(1):
        lista_animales.append([])
        for pos2 in range(valor):
            edad = int(input(f'Cuantos años tiene el Elefante #{pos2+1}: '))
            lista_animales[pos].append(edad)
    print(lista_animales)


def edadChimpance(valor, animal):
    edad = 0
    for pos in range(1):
        lista_animales.append([])
        for pos2 in range(valor):
            edad = int(input(f'Cuantos años tiene el Elefante #{pos2+1}: '))
            lista_animales[pos].append(edad)
    print(lista_animales)


def verificarPorcentaje(animal, valor):
    lista_porcentaje = [0, 0, 0]
    suma = 1
    edad = 0
    for pos in range(1):
        for pos2 in range(valor):
            edad = lista_animales[pos][pos2]
            if edad >= 0 and edad <= 1:
                lista_porcentaje[0] += suma
            if edad > 1 and edad <= 3:
                lista_porcentaje[1] += suma
            if edad > 3:
                lista_porcentaje[2] += suma
    print(f'{animal} con edades de 0 a 1 años: {(lista_porcentaje[0]/20)*100}%')
    print(f'{animal} con edades de mas de 1 a 3 años: {(lista_porcentaje[1]/20)*100}%')
    print(f'{animal} con edades mas de 3 años: {(lista_porcentaje[2]/20)*100}%')


while menu != 4:
    menu = int(input("\nMENU\n"
                     "-------------------------------------------\n"
                     "Que desea hacer?\n"
                     "1. Verificar promedio del Elefante\n"
                     "2. Verificar promedio de la Jirafa\n"
                     "3. Verificar promedio del Chimpancés\n"
                     "4. Salir\n"))
    if (menu == 1):
        print("Tomaremos una muestra de 20 elefantes\n"
              "---------------------------------------")
        animal = 'Elefante'
        valor = 20
        lista_animales.clear()
        lista_porcentaje.clear()
        edadElefante(valor, animal)
        verificarPorcentaje(animal, valor)
    if (menu == 2):
        print("Tomaremos una muestra de 15 jirafas")
        animal = 'Jirafa'
        valor = 15
        lista_animales.clear()
        lista_porcentaje.clear()
        edadJirafa(valor, animal)
        verificarPorcentaje(animal, valor)
    if (menu == 3):
        print("Tomaremos una muestra de 40 Chimpancé")
        animal = 'Chimpanse'
        valor = 40
        lista_animales.clear()
        lista_porcentaje.clear()
        edadChimpance(valor, animal)
        verificarPorcentaje(animal, valor)
