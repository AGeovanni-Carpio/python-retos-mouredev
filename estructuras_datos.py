'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
'''
#Los tipos de estructuras de datos que tenemos en Python son
#Listas, un conjunto de faatos ordenados y mutables
#Tuplas, similar a las listas, pero una vez creados ya no se pueden modificar
#Diccionarios, como su nombre lo indica, hay una clave y un valor
#Y conjuntos,que es una lista especial pero que no permite datos repetidos
#Si bien las listas no son igual a los arrays en Java, pueden algo bastante similar, además 
#de que su sintaxis es similar, veamos
familia = ["Alvaro", "America", "Geovanni", "Camila", "Jenifer", "Bruno", "Puky"]
#Pero también se pueden guardar cosas diferentes
casa = [17, "Manati", 30, 17.5, True]
#Y para recorrer hay formas, en Python se le conoce como revanamiento
print(familia[0])
#Ahora más dinámico
for i in range(len(familia)):
    print(f"{int(i + 1)}. {familia[i]}")
'''
Tomar a consideración que el tamaño o len de una lista va de 0 hasta n-1
Donde n es la cantidad de elementos 
En el caso de familia es 7-1 = 6
Veamos que pasa sí ponemos 7 y 8
'''
try:
    print(familia[7])
    print(familia(8))
except IndexError:
    print("Estás intentando usar indice no existentes en tu lista")
finally:
    print("Vemos la importancia de verificar la cantidad de items")
    print(len(familia))
#len() regresa el numero de items, pero en el for, si usamos for i in range(len(lista))
#Se traduce a para indice en el rango de 0 a tamaño - 1 en saltos de 1 en 1
#Veamos que pasa con la siguiente lista 
for i in range(len(casa)):
    print(f"{i + 1}. {casa[i]}")
#Funciona sin problemas, ahora podemos hacer lo siguiente
print(casa[-1])
#Se usa -1 hasta -n para usar la lista al revés
for i in range(-1, -len(casa)-1, -1):
    print(f"{-i}. {casa[i]}")