def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'

    resultado = ''

    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    
    return resultado

cadena = input("Ingrese una cadena de texto: ")

resultado = omitir_vocales(cadena)

print("Cadena resultante:", resultado)