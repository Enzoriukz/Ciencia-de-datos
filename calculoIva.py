''' 
Análisis general: A partir de un cierto monto bruto necesitamos calcular el precio final sumando al monto anterior el porcentaje de Iva sobre el monto inicial.
Datos (lo conocido): monto inicial, valor del IVA 21%                                                                                                                                                                                                  
Resultados (lo esperado): precio final
Relaciones y subproblemas: suma del precio bruto más el porcentaje de iva sobre el precio bruto
'''       

#Definimos los datos
minicial=float(input("Ingrese el precio bruto: "))
tasaiva = 21  # Tasa del IVA del 21%

# Calculamos el precio final
montoiva = minicial + minicial*tasaiva/100

# Imprimimos el resultado
print("El precio final con IVA es:", montoiva)
