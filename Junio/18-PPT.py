# Juego de piedra papel o tijeras
import random as ran
print("""  _                                                                     
 |_) o  _   _| ._ _.     ._   _. ._   _  |    _    _|_ o o  _  ._ _.  _ 
 |   | (/_ (_| | (_| o   |_) (_| |_) (/_ |   (_)    |_ | | (/_ | (_| _> 
                     /   |       |                      _|""")

turnos = int(input("A cuantos turnos quieres jugar?: "))

while turnos != 0:
        turnos = turnos-1
        opciones = ["Piedra","Papel","Tijeras"]
        eleccion_usuario = int(input("""Elija un numero
              1- Piedra 2-Papel 3-Tijeras
              -> """))-1 
        eleccion_computadora = ran.randint(0,2)

        if eleccion_computadora == eleccion_usuario:
                print(f"Usuario:{opciones[eleccion_usuario]}   Computadora: {opciones[eleccion_computadora]}")
                print("Ha habido un empate!")
        elif eleccion_usuario == 1 and  eleccion_computadora == 3:
                print(f"Usuario:{opciones[eleccion_usuario]}   Computadora: {opciones[eleccion_computadora]}")
                print("Has ganado, felicidades!")       
        elif eleccion_usuario == 2 and  eleccion_computadora == 1:
                print(f"Usuario:{opciones[eleccion_usuario]}   Computadora: {opciones[eleccion_computadora]}")
                print("Has ganado, felicidades!")
        elif eleccion_usuario == 3 and  eleccion_computadora == 2:
                print(f"Usuario:{opciones[eleccion_usuario]}   Computadora: {opciones[eleccion_computadora]}")
                print("Has ganado, felicidades!")  

        else:
            print(f"Usuario:{opciones[eleccion_usuario]}   Computadora: {opciones[eleccion_computadora]}")
            print("Has perdido, suerte la proxima!")
        print("   ")

