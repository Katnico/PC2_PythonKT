numeros_encontrados = []

numero = 1500
while numero <= 2700:
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_encontrados.append(numero)
    
    numero += 1

print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_encontrados)