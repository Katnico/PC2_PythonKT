def contar_digitos(numero, digito):
    numero_str = str(numero)
    
    contador = 0

    for d in numero_str:
        if d == str(digito):
            contador += 1
            
    return contador

numero = 2024520
digito = 2
cantidad = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {cantidad}")