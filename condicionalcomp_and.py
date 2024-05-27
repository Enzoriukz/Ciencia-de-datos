'''Condicional parcial (solo el if) con expresión lógica compuesta (and)
Puede ser un ejemplo donde se den si o si dos condiciones para que muestre un mensaje'''
                                                             
numero=int(input("Escriba un número para verificar si tiene una sola cifra: "))
if numero >-10 and numero < 10:
    print("El número tiene una sola cifra")