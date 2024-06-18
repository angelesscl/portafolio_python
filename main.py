# modulos
import os
from lista_opciones import *
from calculadora import programa_calculadora
from conversor import *
from frecuencias import grafica_frecuencias

# INICIO DEL PROGRAMA
os.system("cls")

# lista de opciones
lista_de_opciones = [
    "Calculadora",
    "conversor de monedas",
    "Graficar frecuencias",
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
             conversor_de_monedas
        elif respuesta == "3":
            lista = [
            {"producto": "tomate    ", "f":20},
            {"producto": "coliflor  ", "f":30},
            {"producto": "Espinaca  ", "f":25},
            {"producto": "Apio      ", "f":20}
            ]
            grafica_frecuencias(lista)
        elif respuesta == "10":
             print("[FIN DEL PROGRAMA]")
             break

    except: #SI HAY ERROR
            print("valor nulo")
