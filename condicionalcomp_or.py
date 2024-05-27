'''Condicional completo (if - else) con expresión lógica compuesta (or)
Puede ser una condición donde  se devuelve un mensaje si se da una condición o la otra.
Como el 0 y el 1 no son primos podemos poner esa condición para después determinar 
con otra condición si un numero puede ser primo o compuesto'''
            
numero=int(input("Escriba un número para determinar si puede ser primo o cumpuesto: "))                                                       
if numero == 0 or numero == 1:                                                                                           
    print("El número no es primo ni compuesto")
else:
    print("El número es primo o compuesto")