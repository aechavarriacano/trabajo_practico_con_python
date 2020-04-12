from collections import Counter

archivo_texto = open('test.txt', 'r')
texto = archivo_texto.read()
archivo_texto.close()

palabras = texto.split()

contador = Counter(palabras)

palabra_fracuente = contador.most_common()[0][0]

ocurrencias = texto.count(palabra_fracuente)

print(" La palabra mas frecuente es: %s" % palabra_fracuente, ", porque se encuentra %s" % ocurrencias, " veces")