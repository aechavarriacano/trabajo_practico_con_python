cad = input(' Escribe la frase: ')

cuenta = 0
cuenta2 = 0
cuenta3 = 0
cuenta4 = 0
cuenta5 = 0

for carac in cad:
    if carac == 'a':
        cuenta += 1
    if carac == 'e':
        cuenta2 += 1
    if carac == 'i':
        cuenta3 += 1
    if carac == 'o':
        cuenta4 += 1
    if carac == 'u':
        cuenta5 += 1
print('Existen:', cuenta, 'a,', cuenta2, 'e, ', cuenta3, 'i.', cuenta4, 'o.', cuenta5, 'u.')

