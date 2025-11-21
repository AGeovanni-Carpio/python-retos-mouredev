#Primer ejercicio, dibujar un cuadrado de altura variable con *s
def dibujar_cuadrado(altura):
    for i in range(altura):
        for j in range(altura):
            print("*", end="  ")
        print()    
        
#Segundo ejercicio, dibujar un triangulo rectangulo de altura n
def dibujar_triangulo(altura):
    for i in range(1, altura + 1):
        for j in range(i):
            print("*", end ="")
        print()
#Tercer ejercicio, invertir el ejercicio anterior
def triangulo_invertido(altura):
    for i in range(altura, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
#Cuarto ejercicio, imprimir una piramide
def dibujar_piramide(altura):
    espacios = altura - 1 
    for i in range(1, altura + 1):
        for j in range(espacios):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end = "")
        print()
        espacios -= 1
       
"""
¡Excelente iniciativa! Cerrar la semana con estos tres ejercicios va a solidificar tu lógica de bucles anidados antes de que volvamos a la arquitectura del proyecto el lunes.

Aquí tienes los enunciados redactados con un enfoque de ingeniería, listos para tu libreta o tu Trello.

1. El Triángulo de Floyd (Control de Estado)
Objetivo: Crear una función que imprima una secuencia numérica continua organizada en forma triangular. Requisito Lógico: Debes usar bucles anidados para la estructura y una variable externa (contador) que no se reinicie con los bucles. Input: Un número entero n (filas). Output Esperado (para n=5):

Plaintext

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
2. La Pirámide Invertida (Geometría Negativa)
Objetivo: Crear una función que dibuje una pirámide centrada que "cuelgue" del techo. Requisito Lógico: Debes dominar la relación inversa entre la fila actual y los espacios. A medida que bajas de fila, los espacios aumentan y las estrellas disminuyen. Input: Un número entero n (altura). Output Esperado (para n=5):

Plaintext

*********
 *******
  *****
   ***
    *
3. El Triángulo de Pascal (Matriz y Cálculo)
Objetivo: Generar los coeficientes binomiales donde cada número es la suma de los dos números directamente encima de él. Requisito Lógico:

Backend: Una función que genere una lista de listas [[1], [1,1], [1,2,1]...] sin imprimir nada.

Frontend: Una función separada que reciba esa lista y la imprima centrada. Input: Un número entero n (filas). Output Esperado (para n=5):

Plaintext

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""       
dibujar_cuadrado(5)
dibujar_triangulo(5)
triangulo_invertido(5)
dibujar_piramide(5)