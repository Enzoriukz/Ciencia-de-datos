//Análisis general: A partir de las notas de cada materia necesita calcular el promedio sumando el valor de las notas y dividiendo por la cantidad de notas, en este caso son 5.
//Datos (lo conocido): las 5 notas                                                                  
//Resultados (lo esperado): promedio
//Relaciones y subproblemas: suma del valor de las notas y división por 5

Algoritmo promedio5notas
	Definir nota1,nota2,nota3,nota4,nota5 Como Entero
	Definir promedio Como Real
	Escribir "Ingrese 5 notas para calcular su promedio"
	Leer nota1
	Leer nota2
	Leer nota3
	Leer nota4
	Leer nota5
	promedio=(nota1+nota2+nota3+nota4+nota5)/5
	Escribir "El promedio es: " promedio
FinAlgoritmo
