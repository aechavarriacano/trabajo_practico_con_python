i = 1
estatura=0
suma=0
promedio=0
lista = []
terminar = False
while True:
    estatura=input("Ingresar estatura de persona %s: " %(i))

    if estatura == "":
        terminar = True
    else:
        terminar = False
        lista.append(int(estatura))

    if terminar:
        break

    i = i + 1


for x in lista:
    suma = suma + x
    print(suma)

if len(lista) > 0 : promedio = suma / len(lista)

print(lista, "Suma: %d" %(suma) + " Promedio: %d" % (promedio) )