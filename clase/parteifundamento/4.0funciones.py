#funciones y uso de la PEP8
# PEP8 es una guia de estilo para escribir codigo en python, que establece una serie de reglas y recomendaciones para mejorar la legibilidad y mantenibilidad del codigo. Algunas de las reglas mas importantes de la PEP8 son:
# - Usar nombres de variables y funciones en minusculas, con palabras separadas por gu
# iones bajas (snake_case)
# - Usar espacios en blanco para mejorar la legibilidad del codigo, por ejemplo, alrededor
# de los operadores, despues de las comas, etc.
# - Usar indentacion de 4 espacios para indicar los bloques de codigo, por ejemplo
#   en las funciones, condicionales, bucles, etc.
# - Usar lineas en blanco para separar las funciones y las clases, y para separar
# los bloques de codigo dentro de las funciones.
# - Usar comentarios para explicar el codigo, especialmente en las partes mas complejas o importantes
# - Usar docstrings para documentar las funciones, clases y modulos, describiendo
# su proposito, sus parametros, su valor de retorno, etc.
# - Evitar el uso de caracteres especiales, como acentos, eñes, etc
# - Evitar el uso de palabras reservadas como nombres de variables o funciones, como por ejemplo, def, class, if, else, etc.
# - Evitar el uso de
#   nombres de variables o funciones que sean demasiado cortos o demasiado largos, o que no sean descriptivos, como por ejemplo, x, y, z, a, b, c, etc.
# - Evitar el uso de espacios en blanco al final de las lineas, o entre los paréntesis, corchetes o llaves, como por ejemplo, ( 1 + 2 ), [ 1, 2, 3 ], { 'a': 1, 'b': 2 }, etc.
# - Evitar el uso de lineas demasiado largas, que superen los 79 caracteres, para mejorar la legibilidad del codigo en diferentes dispositivos o editores.
# usar tipe hints para indicar el tipo de dato de las variables, parametros y valores de retorno de las funciones, como por ejemplo, def suma(a: int, b: int) -> int: return a + b
# 
#funciones
def suma(a: int, b: int) -> int: #definicion de una funcion que recibe dos parametros de tipo int y devuelve un valor de tipo int
    """Esta funcion recibe dos numeros enteros y devuelve su suma""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    if a == 0: #condicion para verificar si el primer numero es cero
        return b #valor de retorno de la funcion, que es el segundo numero si el primer numero es cero
    return suma(a+b,b)#valor de retorno de la funcion, que es la suma de los dos numeros enteros
def resta(a: int, b: int) -> int: #definicion de una funcion que recibe dos parametros de tipo int y devuelve un valor de tipo int
    """Esta funcion recibe dos numeros enteros y devuelve su resta""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    return a - b #valor de retorno de la funcion, que es la resta de los dos numeros enteros
def multiplicacion(a: int, b: int) -> int: #definicion de una funcion que recibe dos parametros de tipo int y devuelve un valor de tipo int
    """Esta funcion recibe dos numeros enteros y devuelve su multiplicacion""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    return a * b #valor de retorno de la funcion, que es la multiplicacion de los dos numeros enteros   
def division(a: int, b: int) -> float: #definicion de una funcion que recibe dos parametros de tipo int y devuelve un valor de tipo float
    """Esta funcion recibe dos numeros enteros y devuelve su division""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    if b == 0: #condicion para evitar la division por cero
        return float('inf') #valor de retorno de la funcion, que es infinito si el divisor es cero
    return a / b #valor de retorno de la funcion, que es la division de los dos numeros enteros
numero1 = int(input("Ingrese el primer numero entero: ")) #entrada de datos por teclado y conversion a int
numero2 = int(input("Ingrese el segundo numero entero: ")) #entrada de datos por teclado y conversion a int
print("La suma de los dos numeros es: ", suma("feo", numero2)) #salida de datos por pantalla usando la funcion suma
print("La resta de los dos numeros es: ", resta(numero1, numero2)) #salida de datos por pantalla
#Investigacion  
#Inv 4.0 Funciones recursivas
#Realizar una investigacion sobre las funciones recursivas en python, que es una funcion que se llama a si misma, y mostrar ejemplos de su uso en diferentes situaciones, como por ejemplo, calcular el factorial de un numero, calcular la serie de Fibonacci, etc. 
#Inv 4.1  Diferencia entre funciones por referencia y por valor
#Realizar una investigacion sobre la diferencia entre funciones por referencia y por valor en python, que es la forma en que se pasan los parametros a las funciones, y mostrar ejemplos de cada caso, como por ejemplo, pasar una lista a una funcion y modificarla dentro de la funcion, o pasar un numero a una funcion y modificarlo dentro de la funcion, etc.

#Proyecto:
#4.0 ) Escriba un programa que implemente el flujo de mensajes desde la capa más alta hasta la capa más baja del
#modelo de protocolos de siete capas. Su programa debe incluir una función de protocolo separada para cada
#capa. Los encabezados de los protocolos son secuencias de hasta 64 caracteres. Cada función de protocolo tiene
#dos parámetros: un mensaje que se pasa del protocolo de la capa superior (un búfer de caracteres) y el tamaño
#del mensaje. Esta función añade su encabezado al frente del mensaje, imprime el nuevo mensaje en la salida
#estándar y después invoca a la función de protocolo del protocolo de la capa inferior. La entrada del programa es
#un mensaje de aplicación (una secuencia de 80 caracteres o menos).

#Se debe aplicar los conceptos visto: funciones, condiciones, bucles, operadores, tipos de datos primitivos, entrada y salida de datos.