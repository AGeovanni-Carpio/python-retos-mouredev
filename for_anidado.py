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
       
dibujar_cuadrado(5)
dibujar_triangulo(5)
triangulo_invertido(5)
dibujar_piramide(5)