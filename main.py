# modulos
import os
from lista_opciones import *
from calculadora import programa_calculadora
from conversor import *

# INICIO DEL PROGRAMA
os.system("cls")

# lista de opciones
lista_de_opciones = [
    "Calculadora",
    "conversor de monedas",
    "Opción 3",
    "Opción 4",
    "Opción 5",
    "Opción 6",
    "Opción 7",
    "Opción 8",
    "Opción 9",
    "Salir"
]

while True:
    cargar_opciones(lista_de_opciones)


# EJECUTO MI PROGRAMA ESPERANDO UN POSIBLE ERROR
    try: # SI NO HAY ERRORES
        respuesta = input("[?] ")

        if respuesta == "1":
            programa_calculadora()
        elif respuesta == "2":
             conversor_de_monedas()
        elif respuesta == "10":
             break

    except: #SI HAY ERROR
            print("valor nulo")
