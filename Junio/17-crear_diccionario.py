# Programa creador de diccionario
# Pretendamos que estamos jugando tutifruti con la letra C
# Declaramos las variables
claves = ["Nombre","Apellido","Color","Comida","Pais","Ciudad","Pelicula","Famoso"]
valores = ["Claudia","Caceres","Celeste","Caldo","Colombia","Cartagena","Cars","Charlie Chaplin"]
diccionario = {}

# Las almacenamos en un diccionario
for i in range(7):
    diccionario[claves[i]] = valores[i]

# Mostramos los resultados 
print("""_  _ _  _ ____ ____ ___ ____ ____    ___  _ ____ ____ _ ____ _  _ ____ ____ _ ____ 
|\ | |  | |___ [__   |  |__/ |  |    |  \ | |    |    | |  | |\ | |__| |__/ | |  | 
| \| |__| |___ ___]  |  |  \ |__|    |__/ | |___ |___ | |__| | \| |  | |  \ | |__|""")

print(diccionario)

print("Accedemos a un valor especifico para comprobar: Pelicula")

print(diccionario["Pelicula"])