cantidades = 0
menor_que_cero = 0
mayor_que_cero = 0
lista = []

cantidades = int(input("Cantidad de datos: "))
for i in range(0, cantidades):
    cantidad=int(input("Ingresar cantidad %d: " %(i + 1)))
    if cantidad >= 0 :
        mayor_que_cero = mayor_que_cero + 1
    else:
        menor_que_cero = menor_que_cero + 1


print(" Mayores a cero: %d" %(mayor_que_cero) + " Menores a cero: %d" %(menor_que_cero))

