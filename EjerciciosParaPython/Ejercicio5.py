n = 0
pares = ''
impares = ''
producto_pares = 0
producto_impares = 0
while n < 100:
    if n% 2 == 0:
        pares += ' %i ' %n
    n += 1
    producto_pares *= n

    if n% 1 == 0:
        impares += ' %i ' %n
    n += 1
    producto_impares *= n
print("Los numeros pares del 0 al 100 son: ", pares)
print("la multriplicacion de los numeros pares es: ", producto_pares)
print("Los numeros impares del 0 al 100 son: ", impares)
print("la multriplicacion de los numeros impares es: ", producto_impares)
