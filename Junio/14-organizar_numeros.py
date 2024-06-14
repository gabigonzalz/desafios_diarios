# Programa sorteador de numeros
print(""".__.                     .          .                            
|  |._. _  _.._ *__. _. _| _ ._.   _| _   ._ . .._ _  _ ._. _  __
|__|[  (_](_][ )| /_(_](_](_)[    (_](/,  [ )(_|[ | )(/,[  (_)_) 
       ._|""")

# Declaramos las variables necesarias
cant_numeros = int(input("Cuantos numeros vas a ingresar?: "))
numeros = []

# Pedimos los numeros al usuario
for i in range(cant_numeros):
    while True:  # Bucle hasta que se ingrese un valor valido
        try:
            numero_ingresado = int(input(f"Ingrese el número entero {i+1}*: "))
            numeros.append(numero_ingresado)
            break  # Sale si se ingreso un numero valido
        except ValueError:
            print("Lo ingresado no es un número! Intente de nuevo.")

# Organizamos los numeros e imprimimos
numeros.sort()
print(f"Tus números organizados son: {numeros}")