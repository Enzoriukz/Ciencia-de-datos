'''
Diseñar un programa completo (Pseudocódigo, Diagrama de Flujo y Código en Python) 
que permita ingresar un monto en Pesos ARS y devuelva como resultado el equivalente en Dólares USD.
'''
montoars = float(input("Ingrese el monto en Pesos ARS: "))
valordecambio = 0.0011  # 1peso = 0,0011 dolares

print("El equivalente en Dólares USD es:", montoars*valordecambio)
