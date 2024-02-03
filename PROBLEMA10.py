def obtener_fecha_en_formato_iso(fecha):
    partes = fecha.split()

    año = partes[-1]

    if len(partes) == 3:
        mes = partes[0]
        dia = partes[1][:-1]  
    else:  
        mes = partes[0]
        dia = partes[1][:-1]  

    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04", 
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08", 
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }
    mes_numero = meses[mes]

    dia = f"{int(dia):02}"

    fecha_iso = f"{año}-{mes_numero}-{dia}"
    
    return fecha_iso

fecha_usuario = input("Ingrese una fecha (mes-día-año o mes día, año): ")

fecha_iso = obtener_fecha_en_formato_iso(fecha_usuario)

print("Fecha en formato AAAA-MM-DD:", fecha_iso)