cantidad_alumnos = 0
lista = []
suma = 0
promedio = 0
terminar = False
while True:
    cantidad_alumnos = int(input("Cantidad de Alumnos: "))
    for i in range(0, cantidad_alumnos):
        edad_alumno=int(input("Ingresar edad alumno %d: " %(i + 1)))
        if edad_alumno < 18 :
            lista.append(edad_alumno)
        else:
            break

    for x in lista:
        suma = suma + x

    if len(lista) > 0 : promedio = suma / len(lista)

    print(lista, " La suma es: %d" %(suma) + " el promedio es: %d" %(promedio))

    if input("Desea Continuar? y/n: ") == "n":
        terminar = True
    else:
        terminar = False
        cantidad_alumnos = 0
        lista = []
        suma = 0
        promedio = 0

    if terminar:
        break
