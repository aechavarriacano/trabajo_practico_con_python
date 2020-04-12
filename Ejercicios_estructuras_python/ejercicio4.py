texto = str(input("Ingrese una palabra: "))

if str(texto) == str(texto)[::-1]:
    print("Es palindroma")
else:
    print("No es palindroma")