# Programa que cuenta vocales
print("""          ,      .          .                  .      
 _. _ ._ -+- _. _| _ ._.   _| _   .  , _  _. _.| _  __
(_.(_)[ ) | (_](_](_)[    (_](/,   \/ (_)(_.(_]|(/,_)""")
# Le pedimos al usuario una frase, declaramos las vocales y el contador
frase = str(input("Ingrese una frase: "))
vocales = "aeiou"
contador = 0
# Checkeamos cada letra de la frase
for i in frase:
    if i in vocales:
        contador += 1
    else:
        continue
# Imprimimos el resultado
print(f"En tu frase hay {contador} vocales.")