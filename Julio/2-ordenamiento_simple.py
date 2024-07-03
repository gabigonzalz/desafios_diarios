# 03/07/24
# Ordenamiento de busqueda por seleccion

def ordenamiento_seleccion(lista):
    for i in range(len(lista) - 1): # Iteramos todos los elementos
        menor = i # Agarramos el primer elemento

        for j in range(i + 1, len(lista)): # Iteramos el RESTO de los elementos
            if lista[j] < lista[menor]: # Si el iterador j es mas chico que 'menor'
                menor = j # Guardamos como menor

        if menor != i: # Si menor no es el elemento default
            lista[menor], lista[i] = lista[i], lista[menor] # Intercambiamos los elementos

numeros = [13, 27, 12, 66, 2, 45, 90, 10345, -1, -3, 0]
print(f"""Esta es tu lista:
      {numeros}""")

ordenamiento_seleccion(numeros)

print(f"""Esta es tu lista ordenada
      {numeros}""")