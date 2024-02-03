def ingresar_alumnos():
    lista_alumnos = []

    num_alumnos = int(input("Ingrese el número de alumnos: "))

    for i in range(num_alumnos):
        alumno = input(f"Ingrese el nombre del alumno {i+1}: ")
        notas = []

        materia = 1
        while materia <= 3:
            nota = float(input(f"Ingrese la calificación {materia} del alumno {alumno}: "))
            notas.append(nota)
            materia += 1

        alumno_data = {"Alumno": alumno, "Notas": notas}
        lista_alumnos.append(alumno_data)

    return lista_alumnos

def mostrar_listado_alumnos(lista_alumnos):
    print("\nListado completo de alumnos:")
    for alumno in lista_alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

lista_alumnos = ingresar_alumnos()

mostrar_listado_alumnos(lista_alumnos)