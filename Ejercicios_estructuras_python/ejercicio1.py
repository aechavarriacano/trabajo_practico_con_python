calificaciones = {'matematicas':5, 'ingles':4.5, 'espanol':3, 'estadistica':4}
tupla = (calificaciones.values())

suma = 0
for val in tupla:
    suma = suma + val

promedio = 0
promedio = suma/len(calificaciones)

print("El promedio es : ", promedio)
