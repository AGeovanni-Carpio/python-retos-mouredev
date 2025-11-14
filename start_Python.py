#https://www.python.org/
"""Este es
un comentario de varias
líneas en Python."""
'''Este es otro comentario
de varias líneas en Python.
Con comillas simples.'''

mi_primer_variale = "Hola, Mundo!"

#No existen las constantes en Python, 
#Pero se pueden definir variables en mayúsculas para indicar que no deben cambiarse.

PI = 3.1416
MI_CONSTANTE = "Geovanni Carpio es mi nombre"

#En Python existen datos primitivos como:
#Números enteros (int)
edad = 25
#Podemos observar ue no hay una definición cómo lo sería en Java: int edad = 25;
#Tenemos otro tipo de dato muy importante, para manejar números con decimales (float)
altura = 1.80
#Lo que nos servira mucho, serán los datos booleanos (bool)
es_estudiante = False
es_trabajador = True
#Se debe de escribir True o False con la primera letra en mayúscula.
#Finalmente tenemos las cadenas de texto (str)
accion = "Aprendiendo Python"
#Es una enorme ventaja, pues hay más tipos de datos, pero Python lo hará por nosotros.
#Por ejemplo, si queremos definir una variable con un número decimal,
#Python automáticamente la reconocerá como un dato float.   
#Algo no muy utilizado pero qué es útil conocer es NoneType, que representa la ausencia de valor.
valor_nulo = None
#None se utiliza para indicar que una variable no tiene ningún valor asignado.
#Finalmente, veremos cómo imprimir en consola.
print(mi_primer_variale)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)
print("Acción:", accion)
print("Valor nulo:", valor_nulo)
#La función print() se utiliza para mostrar información en la consola.
#Podemos imprimir tanto variables como texto directamente.
mi_lenguaje_favorito = "Python"
print("Hola, ", mi_lenguaje_favorito)
#También podemos utilizar f-strings para formatear cadenas de texto de manera más sencilla.
#Las f-strings permiten incluir variables directamente dentro de las cadenas de texto.
print(f"Hola, {mi_lenguaje_favorito}")
#En este caso, la variable mi_lenguaje_favorito se inserta directamente en la cadena.
#Esto hace que el código sea más legible y fácil de escribir.
#Finalmente hay que considerar el tipo de dato, por lo que podemos utilizar la función type()
print("El tipo de dato de mi_lenguaje_favorito es:", type(mi_lenguaje_favorito))
print("El tipo de dato de edad es:", type(edad))
print("El tipo de dato de altura es:", type(altura))
print("El tipo de dato de es_estudiante es:", type(es_estudiante))
print("El tipo de dato de valor_nulo es:", type(valor_nulo))
#La función type() devuelve el tipo de dato de la variable o valor que se le pase como argumento.
#Esto es útil para verificar y entender qué tipo de datos estamos manejando en nuestro código.
#Con esto hemos cubierto los conceptos básicos de variables y tipos de datos en Python.
#¡Feliz programación!