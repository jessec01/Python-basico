#bucles 
#for 
#while

#usando while para imprimir los numeros del 0 al 4
x = 0
while x < 5:
    print(x) #imprime el valor de x en cada iteracion del bucle
    x += 1 #incrementa el valor de x en 1 en cada iteracion del bucle   
 #12345
#usando for para imprimir los numeros del 0 al 4
for i in range(5): #range(5) genera una secuencia de numeros del
    print(i) #imprime el valor de i en cada iteracion del bucle 

#practica de bucles
#dado un n entrada de un numero entero, imprimir la tabla de multiplicar de ese numero del 1 al 10
for x in range(1, 10): #range(1, 11) genera una secuencia de numeros del 1 al 10
    n= int(input("Ingrese un numero entero: ")) #entrada de datos por teclado y conversion a int
    print(n, "x", x, "=", n*x) #imprime la tabla de multiplicar de n del 1 al 10
for x in range(1, 10): #range(1, 11) genera una secuencia de numeros del 1 al 10
    n= int(input("Ingrese un numero entero: ")) #entrada de datos por teclado y conversion a int
    print(f"{n} x {x} = {n*x}") #imprime la tabla de multiplicar de n del 1 al 10 usando fstring
#Imvestigacion:
#Inv 3.0 Bucles anidados
#Realizar una investigacion sobre los bucles anidados en python, que es un bucle dentro de otro bucle, y mostrar ejemplos de su uso en diferentes situaciones.
#Inv 3.1 Bucles infinitos
#Realizar una investigacion sobre los bucles infinitos en python, que es un bucle que no tiene una condicion de salida o que la condicion de salida nunca se cumple, y mostrar ejemplos de su uso en diferentes situaciones, y como evitar los bucles infinitos.
#ejercicio:
# 3.1) Mostrar la impresion de P(A)= P(A)+P(B)-P(A n B) 
#para la version generalizada con n eventos, mostrar la impresion de P(A1 U A2 U ... U An) = P(A1) + P(A2) + ... + P(An) - P(A1 n A2) - P(A1 n A3) - ... - P(An-1 n An) + P(A1 n A2 n A3) + ... + (-1)^(n+1)P(A1 n A2 n ... n An)

#Ejemplo con 3 eventos: P(A1 U A2 U A3) = P(A1) + P(A2) + P(A3) - P(A1 n A2) - P(A1 n A3) - P(A2 n A3) + P(A1 n A2 n A3)
#mostrar un minimo de impresion de 5 eventos como minimo, y un maximo de impresion de 10 eventos como maximo.
#usando solo bucles y condiciones  sin usar funciones ni librerias externas.