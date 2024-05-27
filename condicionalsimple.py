'''
Condicional parcial (solo el if) con expresión lógica simple
Puede ser una condición donde se devuelva un mensaje si se da una condición.
En este caso queremos que nos diga si el número ingresado es cero
'''
numero=int(input("Escriba un número para verificar si es divisible por 5: "))
if numero % 5 == 0:                                                                                                                         
    print("El número es divisible por 5")