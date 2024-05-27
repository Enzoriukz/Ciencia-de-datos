num = int(input("Ingrese un número: "))
print("Mostrando números pares del 0 al", num, ":")
for i in range(num + 1):
    if i % 2 == 0:
        print(i)
