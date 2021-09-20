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

# Punto#3 ---------------------------------------------------------------

empleados = {}
nombre = ''


def salario(obreros):
    for empleado in range(obreros):
        nombre = 'Empleado #' + str((empleado+1))
        horas = int(input(f"Cuantas horas trabajo el {nombre}: "))
        if (horas < 40):
            pago = horas*20
        elif (horas > 40):
            horas = horas-40
            pago = (horas*25)+(40*20)
        empleados[nombre] = "$" + str(pago)
    print("Este es el listado de pagos que se deben hacer:\n"
          "--------------------------------------------------")
    for empleado in empleados:
        print(f"{empleado}: {empleados[empleado]}")


obreros = int(input("Cuantos empleados tiene: "))
salario(obreros)

# Punto # 4--------------------------------------------------------

lista_alumnos = {}
lista_sexo = [0, 0, 0]


def sexo(alumnos):
    hombre = 0
    mujer = 0
    for alumno in range(alumnos):
        turno = 'Alumno #' + str((alumno+1))
        sexo = int(input(f"Que sexo es el {turno}: \n"
                         "1. Masculino\n"
                         "2. Femenino\n"
                         "Digite la opción: "))
        if (sexo == 1):
            edad = int(input("Cuantos años tiene el alumno: "))
            lista_sexo[0] += edad
            sexo = 'Masculino'
            conteo = 1
            hombre += conteo
        elif (sexo == 2):
            edad = int(input("Cuantos años tiene la alumna: "))
            lista_sexo[1] += edad
            sexo = 'Femenino'
            conteo = 1
            mujer += conteo
    print(f"Hay en total {alumnos} alumnos:\n Sacaremos el "
          "promedio de sus edades\n"
          "--------------------------------------------------\n")
    for valor in range(1):
        print(f"HOMBRES------------\n"
              f"Edades: {lista_sexo[0]}\n"
              f"Cantidad: {hombre}\n"
              f"Promedio: {lista_sexo[0]/hombre}")
        print(f"\nMUJERES------------\n"
              f"Edades: {lista_sexo[1]}\n"
              f"Cantidad: {mujer}\n"
              f"Promedio: {lista_sexo[1]/mujer}")
        print(f"\nSALON--------:"
              f"Edades: {(lista_sexo[1]+lista_sexo[0])}\n"
              f"Cantidad: {alumnos}\n"
              f"Promedio: {(lista_sexo[1]+lista_sexo[0])/(alumnos)}")


alumnos = int(input("Cuantos alumnos son: "))
sexo(alumnos)

# Punto #5----------------------------------------------------------------


def mayor(valores):
    mayor = valores[0]
    aux = 0
    for valor in valores:
        aux = valor
        if valor > mayor:
            aux = mayor
            mayor = valor
        print(f"--------\n\n{mayor} es mayor {aux}\n----------")
    print(f"\nEl mayor es {mayor}")


cantidad = int(input("Cuantos numeros desea verificar: "))
valores = []
for valor in range(cantidad):
    dato = float(input(f"Digite el valor del numero {(valor+1)} "))
    valores.append(dato)
mayor(valores)

# Punto #6-----------------------------------------------------------------

pesos_lista = []


def registroPesos():
    for valor in range(3):
        print(f'\nPERSONA #{(valor+1)}')
        pesos_lista.append([])
        for pos in range(3):
            peso = float(input(f"Digite el peso de la báscula #{(pos+1)} "))
            pesos_lista[valor].append(peso)
    print(pesos_lista)


def calculos():
    peso = 0
    for valor in range(10):
        peso = 0
        print(f"\nPERSONA #{(valor+1)}")
        peso_anterior = float(input("Digite el peso de la ultima véz en kg: "))
        for pos in range(10):
            peso += pesos_lista[valor][pos]
        promedio = peso/10
        if (promedio > peso_anterior):
            print(f'Actualmente tiene en promedio un peso de {promedio}kg\n'
                  f'SUBIO {(promedio-peso_anterior)}kg')
        elif (promedio < peso_anterior):
            print(f'Actualmente tiene en promedio un peso de {promedio}\n'
                  'BAJO {(peso_anterior-promedio)}kg')
        else:
            print(f"SE MANTUBO EN {promedio}")


registroPesos()
calculos()
