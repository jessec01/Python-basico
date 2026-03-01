#bucles 
#for 
#while

#usando while para imprimir los numeros del 0 al 4
x = 0
while x < 5:
    print(x) #imprime el valor de x en cada iteracion del bucle
    x += 1 #incrementa el valor de x en 1 en cada iteracion del bucle   
 
#usando for para imprimir los numeros del 0 al 4
for i in range(5): #range(5) genera una secuencia de numeros del
    print(i) #imprime el valor de i en cada iteracion del bucle 

#practica de bucles
#dado un n entrada de un numero entero, imprimir la tabla de multiplicar de ese numero del 1 al 10
for x in range(1, 11): #range(1, 11) genera una secuencia de numeros del 1 al 10
    n= int(input("Ingrese un numero entero: ")) #entrada de datos por teclado y conversion a int
    print(n, "x", x, "=", n*x) #imprime la tabla de multiplicar de n del 1 al 10