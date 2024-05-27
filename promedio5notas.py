'''
Análisis general: A partir de las notas de cada materia necesita calcular el promedio sumando el valor de las notas y dividiendo por la cantidad de notas, en este caso son 5.
Datos (lo conocido): las 5 notas                                                                  
Resultados (lo esperado): promedio
Relaciones y subproblemas: suma del valor de las notas y división por 5
'''

#pedir y leer las 5 notas
print("ingrese 5 notas para calcular su promedio")
nota1=int(input("Ingrese la nota 1: "))
nota2=int(input("Ingrese la nota 2: "))
nota3=int(input("Ingrese la nota 3: "))
nota4=int(input("Ingrese la nota 4: "))
nota5=int(input("Ingrese la nota 5: "))

# Calculo del promedio
promedio=(nota1+nota2+nota3+nota4+nota5)/5

# imprimir el resultado
print("El promedio es:", promedio)