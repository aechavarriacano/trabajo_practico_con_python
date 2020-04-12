frase = input(' Escribe la frase: ')

vocales = 'aeiouAEIOU'
contador = 0

for letra in frase:
    if letra in vocales:
        contador = contador + 1

print("Las cantidad de vocales en la frase son: ", contador)

