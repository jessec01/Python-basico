
#tipos de datos primitivos en python
#price:float 100.0 
# pertence a los tipos de datos primitivos 
price=10.5 #un tipo de dato float 
#edad: int =30 #un tipo de dato int
#edad= #un tipo de dato string
nombre:str = "Juan" #un tipo de dato string
#complex un tipo de dato complejo
es_complejo = True #un tipo de dato booleano
#6+3i es un numero complejo con parte real 6 y parte imaginaria 3
#Operadores
#operadores aritmeticos
suma = 10 + 5 #suma de dos numeros
resta = 10 - 5 #resta de dos numeros
multiplicacion = 10 * 5 #multiplicacion de dos numeros
division = 10 / 5 #division de dos numeros
division_entera = 10 // 3 #division entera de dos numeros
modulo = 10 % 2 #modulo de dos numeros
potencia = 10 ** 2 #potencia de un numero
#simplificacion de expresiones
#suma++
suma += 5 #suma de un numero a una variable
resta -= 5 #resta de un numero a una variable
multiplicacion *= 5 #multiplicacion de un numero a una variable
division /= 5 #division de un numero a una variable
division_entera //= 3 #division entera de un numero a una variable
modulo %= 3 #modulo de un numero a una variable
potencia **= 2 #potencia de un numero a una variable

suma=suma + 5 #es igual a suma += 5
resta=resta - 5 #resta de un numero a una variable
multiplicacion=multiplicacion * 5 #multiplicacion de un numero a una variable
division=division / 5 #division de un numero a una variable     

#operadores de comparacion
igual = 10 == 5 #verifica si dos numeros son iguales
diferente = 10 != 5 #verifica si dos numeros son diferentes
mayor = 10 > 5 #verifica si un numero es mayor que otro
menor = 10 < 5 #verifica si un numero es menor que otro
mayor_igual = 10 >= 5 #verifica si un numero es mayor o igual que otro
menor_igual = 10 <= 5 #verifica si un numero es menor o igual que otro
#operadores logicos
and_logico = True and False #operador logico AND
or_logico = True or False #operador logico OR

not_logico = not True #operador logico NOT
#operadores inclusivos
in_inclusivo = 5 in [1, 2, 3, 4, 5] #verifica si un elemento esta en una lista
not_in_inclusivo = 5 not in [1, 2, 3, 4] #verifica  si un elemento no esta en una lista
#operadores de identidad
a=10
b=a
c=10
is_identidad = a is b #verifica si dos objetos son el mismo objeto
is_not_identidad = a is not c #verifica si dos objetos no son el mismo objeto   
#ENTRADA Y SALIDA DE DATOS
#entrada de datos
nombre_usuario = input("escribe un mensaje:") #entrada de datos por teclado
#Por defecto, la función input devuelve una cadena de texto (string). Si deseas convertir la entrada a otro tipo de dato, puedes usar las funciones de conversión como int(), float(), etc.
edad_usuario = int(input("Ingrese su edad: ")) #entrada de datos por teclado y convers
price_usuario = float(input("Ingrese el precio: ")) #entrada de datos por teclado y conversion a float
#salida de datos
print("Hola, " + nombre_usuario) #salida de datos por pantalla
print("Tu edad es: " + str(edad_usuario)) #salida de datos por pantalla 
print("El precio es: " + str(price_usuario)) #salida de datos por pantalla
#docs python https://docs.python.org/3/library/stdtypes.html#built-in-types
#Investigacion 
#Inv 1.0 el Tamaño de cada tipo de dato 
#Realizar una investigacion sobre el tamaño de cada tipo de dato primitivo en python, por ejemplo, el tamaño de un int, float, string, etc. y mostrar los resultados en pantalla. 
#Inv 1.1 el rango de cada tipo de dato
#Realizar una investigacion sobre el rango de cada tipo de dato primitivo en python, por ejemplo, el rango de un int, float, string, etc. y mostrar los resultados en pantalla.
#Ejercicio
#1.1) Escriba un programa que solicite dos numeros complejos al usuario y realice una suma de ellos e imprima el resultado
