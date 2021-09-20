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
