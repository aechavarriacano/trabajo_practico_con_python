vocales = ("a", "e", "i", "o", "u")
frase = input(' Escribe la frase: ')
nueva_frase = ""

for letra in frase:
    if letra not in vocales:
        nueva_frase = nueva_frase + letra
print("Tu nueva frase es: ", nueva_frase)



