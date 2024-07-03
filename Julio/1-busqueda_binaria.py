# 02/07/24
# Búsqueda en lista ordenada: 
# Implementa una función de búsqueda binaria que determine si un número 
# está en una lista ordenada de 10 elementos.

def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        # Partimos a la mitad
        medio = (inicio + fin) // 2
        # Si el elemento de la mitad es lo que buscamos
        if lista[medio] == elemento:
            return True
        # Si el elemento de la mitad es menor a lo que buscamos
        elif lista[medio] < elemento:
            inicio = medio + 1 # SUbimos
        # Si el elemento de la mitad es mayor a lo que buscamos
        else:
            fin = medio - 1  # Bajamos
    
    return False  

lista_ordenada = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numero_buscar = int(input("Ingrese un numero: "))
    
if busqueda_binaria(lista_ordenada, numero_buscar):
    print(f"El numero {numero_buscar} esta en la lista.")
    print(f"Estos son los numeros: {lista_ordenada}")
else:
    print(f"El numero {numero_buscar} no esta en la lista.")
    print(f"Estos son los numeros: {lista_ordenada}")
