calificaciones = {'matematicas':5,'ingles':4.5,'espanol':3,'estadistica':1}

mayor=0
for clave,valor in calificaciones.items():
    #print("%s -> %s " %(clave,valor))
    if valor >= mayor:
        mayor=valor
        materia_mayor=clave

print("La materia con mejor promedio es: %s " %(materia_mayor))


