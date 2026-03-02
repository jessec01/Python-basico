#tupla
#Una tupla es una estructura de datos similar a una lista, pero inmutable, es decir, no se pueden modificar sus elementos una vez creada.
PI= 3.1416 #constante de la tupla
#lista= [1, 2, 3] #lista de numeros
tupla_vacia = () #tupla vacia
tupla_numeros = (1, 2, 3, 4, 5) #tupla de numeros
tupla_mixta = (1, "hola", 3.14, True)
#acceso a elementos de una tupla
print(tupla_numeros[0]) #acceso al primer elemento de la tupla
print(tupla_numeros[1]) #acceso al segundo elemento de la tupla
for i in range(len(tupla_numeros)): #acceso a todos los elementos de la tupla usando un bucle for y la funcion len() para obtener el tamaño de la tupla
    print(tupla_numeros[i]) #imprime el elemento de la tupla en cada iteracion del bucle
#practica de tupla:
#dado una tupla de numeros, imprimir el numero mayor y el numero menor de la tupla
tupla_numeros = (5, 2, 9, 1, 3) #tupla de numeros
numero_mayor = tupla_numeros[0] #inicializa el numero mayor con el primer elemento de la tupla
numero_menor = tupla_numeros[0] #inicializa el numero menor con el primer elemento de la tupla
for i in range(len(tupla_numeros)): #bucle for para recorrer la tupla y encontrar el numero mayor y el numero menor
    if tupla_numeros[i] > numero_mayor: #condicion para verificar si el elemento de la tupla es mayor que el numero mayor actual
        numero_mayor = tupla_numeros[i] #actualiza el numero mayor con el nuevo valor
    if tupla_numeros[i] < numero_menor: #condicion para verificar si el elemento de la tupla es menor que el numero menor actual
        numero_menor = tupla_numeros[i] #actualiza el numero menor con el nuevo valor
print("El numero mayor de la tupla es: ", numero_mayor) #imprime el numero mayor de la tupla
print("El numero menor de la tupla es: ", numero_menor) #imprime el numero menor de la tupla
#Investigacion
#Inv. 6.0 Rendimiento de tuplas vs listas
#Realizar una investigacion sobre el rendimiento de las tuplas vs las listas en python, que es la diferencia en el tiempo de ejecucion y el uso de memoria entre las tuplas y las listas, y mostrar ejemplos de cada caso, como por ejemplo, crear una tupla y una lista con el mismo contenido y medir el tiempo de ejecucion y el uso de memoria de cada uno, etc.
#Inv 6.1 & Sets Inmutabilidad, namedtuple, operaciones de conjuntos
#Realizar una investigacion sobre las operaciones de conjuntos en python, como por ejemplo, la union, la interseccion, la diferencia, etc. y mostrar ejemplos de cada caso usando tuplas y sets, y tambien investigar sobre las namedtuple en python, que es una tupla con nombre para cada elemento, y mostrar ejemplos de su uso en diferentes situaciones.
#Ejercicio:
#6.1) Escriba un programa que lea una tupla de numeros y calcule la media, la mediana y la moda de los numeros de la tupla, e imprima los resultados en pantalla.
#media es promedio de los numeros de la tupla
#  mediana es el numero que se encuentra en el medio de la tupla ordenada, y 
# moda es el numero que se repite con mayor frecuencia en la tupla.
#1222233444
#media suma/ 11
#mediana 2
#moda  2