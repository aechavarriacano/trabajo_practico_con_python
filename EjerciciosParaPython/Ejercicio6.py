fibonacci = [0,1]
cantidad = 33
for i in range(2,cantidad):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)