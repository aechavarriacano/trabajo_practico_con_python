numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))
numero_4 = int(input("Ingrese el cuarto numero: "))
numero_5 = int(input("Ingrese el quinto numero: "))
numero_6 = int(input("Ingrese el sexto numero: "))
numero_7 = int(input("Ingrese el septimo numero: "))
numero_8 = int(input("Ingrese el octavo numero: "))
numero_9 = int(input("Ingrese el noveno numero: "))
numero_10 = int(input("Ingrese el decimo numero: "))

lista = [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9, numero_10]

suma = 0
for numero in lista:
    suma = suma + numero

print("La suma de los numeros ingresados es : ", suma)