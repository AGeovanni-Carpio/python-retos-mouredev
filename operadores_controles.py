'''
Ejercicio 1.
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

#En este ejercicio aprenderemos los tipos de operadores en Python y las estructuras de control.
#Para demostrar, haremos impresión en pantalla.
#Operadores Aritméticos
print(f"Suma: 5 + 3 = {5 + 3}")
print(f"Resta: 5 - 3 = {5 - 3}")
print(f"Multiplicación: 5 * 3 = {5 * 3}")
print(f"División: 5 / 3 = {5 / 3}")
print(f"Módulo: 5 % 3 = {5 % 3}")
print(f"Exponente: 5 ** 3 = {5 ** 3}")
#Uno no muy conocido y/o usado es el operador de piso
print(f"Piso: 5 // 3 = {5 // 3}")
#Operadores Relacionales
print(f"¿5 es mayor a 3? {5 > 3}")
print(f"¿5 es menor a 3? {5 < 3}")
print(f"¿5 es igual a 3? {5 == 3}")
print(f"¿5 es mayor o igual a 3? {5 >= 3}")
print(f"¿5 es menor o igual a 3? {5 <= 3}")
print(f"¿5 es diferente a 3? {5 != 3}")
#Es muy importante demostrar que los resultados previos imprimiran True o False
#Operadores Bit a Bit
print(f"AND Bit a Bit: 5 & 3 = {5 & 3}")
print(f"OR Bit a Bit: 5 | 3 = {5 | 3}")
print(f"XOR Bit a Bit: 5 ^ 3 = {5 ^ 3}")
print(f"NOT Bit a Bit: ~5 = {~5}")
print(f"Desplazamiento a la izquierda: 5 << 1 = {5 << 1}")
print(f"Desplazamiento a la derecha: 5 >> 1 = {5 >> 1}")
#Ahora continuamos con los siguientes, que son los operadores de asignación
#Estos se usan para cómo su nombre lo indica asignar, y los usaremos para crear nuestras variables.
a=18
print(f"{a}")
a+=5
print(f"{a}")
a-=5
print(f"a volvio a su valor original {a}")
a*=3
print(f"{a}")
a/=3
print(f"Se devuelve a su valor original de a {a}")
#Para evitar confuciones haremos otra variable
b = 45
b%=3
print(f"Se aplico b = b %3: {b}")
a**=2
print(f"Potencia de a^2: {a}")
a//=2
print(f"División entera de a, {a}")
z = 5
z&=1
print(f"Se aplica un and a 'a':{a}")
z|=3
print(f"Se aplica or 3 a 'a': {a}")
z^=3
print(f"Se aplica XOr 3 al valor de a: {a}")
z>>=4
print(f"Se aplica un corrimiento de 4 veces a la derecha al valor de a {a}")
z<<=2
print(f"Ahora un de 2 pero a la izquierda {a}")
#Ahora usemos los lógicos
#En Python solo hay 3 and, or y not
#declaremos dos variables más
c = 4
d = 3
print(f"C and D: {c and d}")
print(f"c or d {c or d}")
print(f"C not D {not d}")

#Operadores de pertenencia in, not in 
#Estos devuelven True o False, ejemplo
cadena = "hola mundo"
print("hola" in cadena)
print("parangacutirimicuaro" in cadena)
print("No estoy" not in cadena, "Ejemplo de No edtoy en cadena")

#Operadores de Identidad is y is not
''''
Hay que resaltar que estos no son muy utilizados, pues va más enfocado a 
la memoria real de la computadora.
'''
var_1 = 0
var_2 = var_1
print(var_1 is var_2)
print("Debe regresar verdadero, pues son el mismo objeto")
#Por esa misma razón es que se llega a confundir, pues son objetos para un
#Principiante debe ser bastante confuso
var_3 = 0
print(var_2 is not var_3)

#Nueva estructura de control
print("\n=== MATCH-CASE (Python 3.10+) ===")
# Ejemplo 1: Básico (como switch)
dia = 3

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6 | 7:  # Múltiples valores
        print("Fin de semana")
    case _:  # Default
        print("Día inválido")

# Ejemplo 2: Con variables
comando = "start"

match comando:
    case "start":
        print("Iniciando sistema...")
    case "stop":
        print("Deteniendo sistema...")
    case "restart":
        print("Reiniciando...")
    case _:
        print("Comando desconocido")

# Ejemplo 3: Pattern matching con tuplas
punto = (0, 0)

match punto:
    case (0, 0):
        print("Origen")
    case (0, y):
        print(f"Eje Y en {y}")
    case (x, 0):
        print(f"Eje X en {x}")
    case (x, y):
        print(f"Punto en ({x}, {y})")

# Ejemplo 4: Con listas
valores = [1, 2, 3]

match valores:
    case []:
        print("Lista vacía")
    case [x]:
        print(f"Un elemento: {x}")
    case [x, y]:
        print(f"Dos elementos: {x}, {y}")
    case [x, y, z]:
        print(f"Tres elementos: {x}, {y}, {z}")
    case _:
        print("Más de tres elementos")

# Ejemplo 5: Con diccionarios
usuario = {"tipo": "admin", "activo": True}

match usuario:
    case {"tipo": "admin", "activo": True}:
        print("Administrador activo")
    case {"tipo": "admin", "activo": False}:
        print("Administrador inactivo")
    case {"tipo": "usuario", "activo": True}:
        print("Usuario normal activo")
    case _:
        print("Otro tipo de usuario")

# Ejemplo 6: Con condiciones (guards)
edad = 23

match edad:
    case x if x < 0:
        print("Edad inválida")
    case x if x < 18:
        print("Menor de edad")
    case x if x < 65:
        print("Adulto")
    case _:
        print("Adulto mayor")

"""El ejemplo anteior, introduce varios conceptos, que iremos descubriendo más adelante
pero, cabe resaltar que es importante conocer esto, pues al venir de otros lenguajes como 
Java que tenemos switch-case, tenemos el match, case y la opción de _ para decir que algo no es valido
esta es una nueva implementación del lenguaje, antes de la 3.9 no existía"""

#No se pide en el ejercicio, pero al ser básico vale la pena, conocer que es necesario entradas de datos 
input("Así se introduce un dato en Python" )
cadena_entrada = input("Introduce una cadena de Texto:" )
print("Tú cadena es: ", cadena_entrada)

#Similar al match tenemos if, elif, else

operacion = int(input("Que operación eliges? " ))
base = 5
if operacion == 1:
    base =+ 5
    print(base)
elif operacion == 2:
    base -= 4
    print(base)
elif operacion == 3:
    base *= 8
    print(base)
elif operacion == 4:
    base /= 0.5
    print(base)
else:
    base **= 9 
    print(base)   

#Ciclos 
#El for es el que mas se usa, y tenemos
#for var in secuencia

recorrido = "hola"
for i in recorrido:
    print(i)
#Luego tenemos range, puede ser range(x), range(x,y) o range(x,y,z)
# Range x es que empieza en 0 hasta x-1
# range x,y es que empieza en x y termina en y
# range x,y,z es para el for como el de Java, la z es el salto que da

for i in range(2,7,1):
    print(i)

#Luego tenemos la parte de while, que es while condicion:

cond = 5

while cond < 10:
    print(cond)
    cond += cond

#Luego tenemos el try-except

try:
    a = 10
    es = 0
    restl = a/es
except ZeroDivisionError:
    print("Recuerda que no podemos dividira a/0")
finally:
    print("De los errores nacen los grandes genios ;)")
    
"""
* Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

#Se usará for por facilidad

for i in range(10,56):
    if ((i%2 == 0) and (i != 16)) and (i%3 != 0):
        print(i)