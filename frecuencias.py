def grafica_frecuencias(lista): # Define una función llamada 'grafica_frecuencias'
    for p in lista:             #  Itera sobre cada elemento 'p' en la 'lista'.
        print(p["producto"], " " ,end="")  # Imprime el valor asociado a la clave 'producto'
        for f in range(p["f"]):  #Itera 'f' veces
            print("0", end="") #Imprime un "0" en cada iteración, sin cambiar de línea.
        print ("")             # Después de imprimir los "0", cambia de línea.

    