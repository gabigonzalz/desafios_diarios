# Pedimos un numero al usuario
numero_ingresado = int(input("Ingrese un numero del 1 al 10: "))
# El titulo de la tabla de multiplicar
print(f"𝐓𝐀𝐁𝐋𝐀 𝐃𝐄 𝐌𝐔𝐋𝐓𝐈𝐏𝐋𝐈𝐂𝐀𝐑 𝐃𝐄𝐋 [ {numero_ingresado} ]")
# Iteramos por todos los numeros en rango 10 y multiplicamos, luego imprimimos
for i in range(10):
    numero_multiplicado = numero_ingresado*(i+1)
    print(f"{numero_ingresado} x {i+1} = {numero_multiplicado}")