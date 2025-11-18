"""
Ejercicio.
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
#Para poder declarar funciones usamos la palabra reserveda def, a continuación un ejemplo de esto.
def funcion_basica():
    print("Hola función")
llamado_funcion = funcion_basica()
#En este primer ejemplo se crea una variable que llama a la función, pues es muy básica
#Pero, después nos daremos cuenta que no es del todo útil 
#Otra forma de llamar a la función es simplemente escribir el nombre de la función
funcion_basica()
#No importa si usamos cadenas o números, se puede hacer lo mismo
def suma_base():
    num_1 = 7
    num_2 = 4.5 
    rest = num_1 + num_2
    print(f"{rest}")
suma_base()
#Luego, vemos que imprime el resultado, pero, ¿Qué pasa si necesitamos que sume los números del usr?
#Usamos parametros

def suma_usr (num_1, num_2):
    rest = num_1 + num_2
    print(rest)
num_1 = int(input("Ingresa el primer número: "))
num_2 = int(input("Ingresa el segundo número: "))
suma_usr(num_1, num_2)
#Cabe resaltar que hay una tercera forma y es más para reutilizar los resultados
def suma_usr_reutilizable (num_1, num_2):
    return num_1 + num_2
print(f"El resultado de nuestra tercera función es {suma_usr_reutilizable(num_1, num_2)}")
#Otro caso es utilizar una funcion sin parametros, pero con return
#Para poder generar otros resultados
def funcion_return():
    return "Hoy es lunes"
hoy_es = funcion_return()
print(f"Mira, {hoy_es}")
#Otros conceptos importantes son
#Los parametros por defecto, lo cual es usado para garantizar que pase lo que pase la función funcionará
def saludar(nombre="Geovanni", hora="mañana"):
    print(f"Buenos días {nombre}, que tengas buena {hora}")

saludar()  # Usa valores por defecto
saludar("Ana")  # Sobrescribe nombre
saludar("Carlos", "tarde")  # Sobrescribe ambos

#Otro par de conceptos a tener en cuenta son los *args y **kwargs
#Los args son utilizados para usar un mismo tipo de dato y manipularlo
#Los kwargs son para meter muktiples tipos de datos, muy útiles para armar JSON
# *args - múltiples argumentos posicionales
def sumar_todos(*numeros):
    return sum(numeros)

print(sumar_todos(1, 2, 3, 4, 5))  # 15

# **kwargs - múltiples argumentos con nombre
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Geo", edad=23, ciudad="CDMX")
#Tenemos 2 tipos de variables para funcionesen Phyton Locales y Globales
#Las locales son para que se afecte únicamente lo que esta dentro de la función 
#Aunque eso último aplica a bucles y condicionales
#Y las gloales que se usan dentro y fuera y prácticamente en cualquier parte del programa
x = 10  # Variable global

def funcion():
    x = 5  # Variable local (diferente a la global)
    print(x)  # Imprime 5

funcion()
print(x)  # Imprime 10 (la global no cambió)

#Otra forma es poder usar y hacer nuestra propia documentación
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base: Ancho del rectángulo
        altura: Alto del rectángulo
    
    Returns:
        float: Área del rectángulo
    """
    return base * altura

# Ver la documentación
help(calcular_area)

#Otra aspecto muy útil es el crear funciones dentro de funciones

def obteniendo_coordenadas(x):
    def coordenada_y (y):
        return x,y
    return coordenada_y(2)
print(f"Coordenadas {obteniendo_coordenadas(5)}")
