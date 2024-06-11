#Programa que invierte caracteres#
print('''dP                                       dP   oo                                                            dP                                       
88                                       88                                                                 88                                       
88 88d888b. dP   .dP .d8888b. 88d888b. d8888P dP 88d888b.    .d8888b. .d8888b. 88d888b. .d8888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. 
88 88'  `88 88   d8' 88ooood8 88'  `88   88   88 88'  `88    88'  `"" 88'  `88 88'  `88 88'  `88 88'  `""   88   88ooood8 88'  `88 88ooood8 Y8ooooo. 
88 88    88 88 .88'  88.  ... 88         88   88 88          88.  ... 88.  .88 88       88.  .88 88.  ...   88   88.  ... 88       88.  ...       88 
dP dP    dP 8888P'   `88888P' dP         dP   dP dP          `88888P' `88888P8 dP       `88888P8 `88888P'   dP   `88888P' dP       `88888P' `88888P"''')
#Definimos una funcion recursiva que recorra la palabra insertada y la invierta
def invertir_caracteres(cadena_de_caracteres):
    #Si se acaba la cadena
    if len(cadena_de_caracteres) == 0:
        return ""
    #LLamamos recursivamente a la funcion y vamos modificando las letras
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])

#Pedimos al usuario una palabra a invertir
palabra = str(input(''',-_/                                                 .      .                                                  .        .      
'  | ,-. ,-. ,-. ,-. ,-. ,-.   . . ,-. ,-.   ,-. ,-. |  ,-. |-. ,-. ,-.   ,-. ,-. ,-. ,-.   . ,-. .  , ,-. ,-. |- . ,-. |  ,-. 
.^ | | | | | |   |-' `-. |-'   | | | | ,-|   | | ,-| |  ,-| | | |   ,-|   | | ,-| |   ,-|   | | | | /  |-' |   |  | |   |  ,-| 
`--' ' ' `-| '   `-' `-' `-'   `-^ ' ' `-^   |-' `-^ `' `-^ ^-' '   `-^   |-' `-^ '   `-^   ' ' ' `'   `-' '   `' ' '   `' `-^ 
          ,|                                 |                            |                                                    
          `'                                 '                            '  
                :            '''))

#Guardamos el resultado dentro de una variable
resultado = invertir_caracteres(palabra)

print("\n")
print(f"Tu palabra invertida es : {resultado} .")
print("\n")