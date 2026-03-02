#condiciones por asignacion
resulatado=10 > 5 #verifica si un numero es mayor que otro y asigna el resultado a una variable
print(resulatado) #imprime el resultado de la condicion
#condiciones por impresion
print(10 > 5) #verifica si un numero es mayor que otro e imprime el resultado de la condicion
#condiciones por control de flujo
#conficion basica if else 
if 10 > 5: #verifica si un numero es mayor que otro y ejecuta un bloque de codigo si la condicion es verdadera
    print("10 es mayor que 5") #imprime un mensaje si la condicion es verdadera
else: #ejecuta un bloque de codigo si la condicion es falsa
    print("10 no es mayor que 5") #imprime un mensaje si la condicion es falsa
#condicion con multiples condiciones elif
if 10 > 5: #verifica si un numero es mayor que otro y ejecuta un bloque de codigo si la condicion es verdadera  
        #bloque de codigo si la condicion es verdadera
    print("10 es mayor que 5") #imprime un mensaje si la condicion es verdadera
elif 10 == 5: #verifica si dos numeros son iguales y ejecuta un bloque de codigo si la condicion es verdadera
    print("10 es igual a 5") #imprime un mensaje si la condicion es verdadera
else: #ejecuta un bloque de codigo si la condicion es falsa
    print("10 no es mayor que 5 ni igual a 5") #imprime un mensaje si la condicion es falsa
#condiciones con operdores logicos
if 10 > 5 and 10 < 20: #verifica si un numero es mayor que otro y menor que otro y ejecuta un bloque de codigo si la condicion es verdadera
#si encuentra una condicion falsa, no ejecuta el bloque de codigo y pasa a la siguiente condicion   
#caso contrario si se usa or 
    print("10 es mayor que 5 y menor que 20") #imprime un mensaje si la condicion es verdadera
else: #ejecuta un bloque de codigo si la condicion es falsa
    print("10 no es mayor que 5 o no es menor que 20") #imprime un mensaje si la condicion es falsa

#practica de condiciones 
#dado la entrada de una accion de juego 
#determinar si es 
#piedra, papel o tijera
#en caso de que no es ninguna de las tres opciones, imprimir un mensaje de error
#entrada de datos input 
accion_juego = input("Ingrese una accion de juego (piedra, papel o tijera): ") #entrada de datos por teclado
if accion_juego == "piedra": #verifica si la accion de juego es piedra y ejecuta un bloque de codigo si la condicion es verdadera
    print("Has elegido piedra") #imprime un mensaje si la condicion es verdadera
elif accion_juego == "papel": #verifica si la accion de juego es papel y ejecuta un bloque de codigo si la condicion es verdadera
    print("Has elegido papel") #imprime un mensaje si la condicion es verdadera
elif accion_juego == "tijera": #verifica si la accion de juego es tijera y ejecuta un bloque de codigo si la condicion es verdadera
    print("Has elegido tijera") #imprime un mensaje si la condicion es verdadera
else: #ejecuta un bloque de codigo si la condicion es falsa
    print("Error: accion de juego no valida") #imprime un mensaje si la condicion es falsa


#Investigacion

#Inv 2.0 Condiciones anidadas
#Realizar una investigacion sobre los errores comunes al usar condiciones anidadas, como por ejemplo, olvidar cerrar un bloque de codigo, o usar una condicion elif sin un bloque de codigo, etc. y mostrar ejemplos de estos errores y como solucionarlos.
#Inv 2.1 Operador ternario
#Realizar una investigacion sobre el operador ternario en python, que es una forma de simplificar una condicion if else en una sola linea de codigo, y mostrar ejemplos de su uso en diferentes situaciones, como por ejemplo, asignar un valor a una variable dependiendo de una condicion, o imprimir un mensaje dependiendo de una condicion, etc.
#ejercicio:
# 2.1) Realizar un programa que simule el funcionamiento de un reloj, usando las condiciones para determinar si es hora, minuto o segundo, y mostrar el mensaje correspondiente. Por ejemplo, si la entrada es 12:30:45, el programa debe imprimir "Es la hora 12", "Es el minuto 30" y "Es el segundo 45". 