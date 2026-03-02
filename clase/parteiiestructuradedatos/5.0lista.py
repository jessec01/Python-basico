#lista 
#python no hay arreglo 
lista_vacia = [] #lista vacia
#comportamientos de lista como un array
lista_numeros = [1, 2, 3, 4, 5] #lista de numeros
lista_numeros[0] #acceso al primer elemento de la lista
lista_numeros[1] #acceso al segundo elemento de la lista
lista_numeros[2] #acceso al tercer elemento de la lista
lista_numeros[3] #acceso al cuarto elemento de la lista
lista_numeros[4] #acceso al quinto elemento de la lista

#en python no exiiste un tipo de dato array, pero se puede usar una lista para simular un array 
lista_mixta = [1, "hola", 3.14, True] #lista mixta de diferentes tipos de datos
#acceso a elementos de una lista
print(lista_numeros[0]) #acceso al primer elemento de la lista
print(lista_numeros[1]) #acceso al segundo elemento de la lista 
for i in range(len(lista_numeros)): #acceso a todos los elementos de la lista usando un bucle for y la funcion len() para obtener el tamaño de la lista
    print(lista_numeros[i]) #imprime el elemento de la lista en cada iteracion del bucle
#pila primero en entrar, primero en salir (LIFO)
# cola  primero en entrar, primero en salir (FIFO)
# arreglo estatico  5 elementos, no se pueden agregar ni eliminar elementos, solo modificar los elementos existentes
# arreglo dinamico lista  se pueden agregar y eliminar elementos dinamicamente
#comportamientos de lista como una pila (stack)
pila = [] #lista vacia que se usara como una pila
pila.append(1) #agrega un elemento al final de la pila
pila.append(2) #agrega un elemento al final de la pila
#comportamientos de lista como una cola (queue)
cola = [] #lista vacia que se usara como una cola
cola.append(1) #agrega un elemento al final de la cola
cola.append(2) #agrega un elemento al final de la cola
cola.pop(0) #elimina el primer elemento de la cola y lo devuelve
#practica de lista:
#dado dos lista de numeros con tamaño fijo de 5 elementos, realizar el comportamiento de maestro y esclavo donde la primera lista es el maestro y la segunda lista es el esclavo, y el maestro controla el comportamiento del esclavo, por ejemplo, si el maestro agrega un elemento a la lista, el esclavo tambien agrega ese elemento a su lista, si el maestro elimina un elemento de la lista, el esclavo tambien elimina ese elemento de su lista, etc.
lista_maestro = [] #lista vacia que se usara como el maestro
lista_esclavo = [] #lista vacia que se usara como el esclavo

def insertar_elemento_maestro(elemento: int) -> None: #definicion de una funcion que recibe un elemento de tipo int y no devuelve nada
    """Esta funcion recibe un elemento de tipo int y lo agrega a la lista maestro, y tambien lo agrega a la lista esclavo""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    lista_maestro.append(elemento) #agrega el elemento a la lista maestro
    lista_esclavo.append(elemento) #agrega el mismo elemento a la lista esclavo
def eliminar_elemento_maestro(elemento: int) -> None: #definicion de una funcion que recibe un elemento de tipo int y no devuelve nada
    """Esta funcion recibe un elemento de tipo int y lo elimina de la lista maestro, y tambien lo elimina de la lista esclavo""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    if elemento in lista_maestro: #condicion para verificar si el elemento esta en la lista maestro
        lista_maestro.remove(elemento) #elimina el elemento de la lista maestro
        lista_esclavo.remove(elemento) #elimina el mismo elemento de la lista esclavo
def mostrar_listas() -> None: #definicion de una funcion que no recibe ningun parametro y no devuelve nada
    """Esta funcion muestra el contenido de la lista maestro y la lista esclavo""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    print("Lista maestro: ", lista_maestro) #imprime la lista maestro
    print("Lista esclavo: ", lista_esclavo) #imprime la lista esclavo
def validar_accion_esclavo() -> None: #definicion de una funcion que no recibe ningun parametro y no devuelve nada
    """Esta funcion valida el comportamiento del esclavo con respecto al maestro, por ejemplo, si el maestro agrega un elemento a la lista, el esclavo tambien agrega ese elemento a su lista, si el maestro elimina un elemento de la lista, el esclavo tambien elimina ese elemento de su lista, etc.""" #docstring de la funcion que describe su proposito, sus parametros y su valor de retorno
    if lista_maestro == lista_esclavo: #condicion para verificar si las listas maestro y esclavo son iguales
        print("El comportamiento del esclavo es correcto") #imprime un mensaje indicando que el comportamiento del esclavo es correcto
    else:
        print("El comportamiento del esclavo es incorrecto") #imprime un mensaje indicando que el comportamiento del esclavo es incorrecto
for i in range(5): #bucle for para agregar elementos a la lista maestro y esclavo
    elemento = int(input("Ingrese un numero entero para la lista maestro: ")) #entrada de datos por teclado y conversion a int
    insertar_elemento_maestro(elemento) #agrega el elemento a la lista maestro y esclavo usando la funcion
validar_accion_esclavo() #valida el comportamiento del esclavo con respecto al maestro usando la funcion
remover_elemento = int(input("Ingrese un numero entero para eliminar de la lista maestro: ")) #entrada de datos por teclado y conversion a int
eliminar_elemento_maestro(remover_elemento) #elimina el elemento de la lista maestro y esclavo usando la funcion
validar_accion_esclavo() #valida el comportamiento del esclavo con respecto al maestro usando la funcion
mostrar_listas() #muestra las listas maestro y esclavo usando la funcion
#Investigacion
#Inv 5.0 Ordenamiento de listas
#Realizar una investigacion sobre los diferentes algoritmos de ordenamiento de listas en python, como por ejemplo, el algoritmo de burbuja, el algoritmo de seleccion, el algoritmo de insercion, el algoritmo de mezcla, el algoritmo de rapido, etc. y mostrar ejemplos de cada algoritmo y su complejidad temporal.
#Inv 5.1  Diferencia entre una lista y un array en terminos de comportamiento, rendimiento y uso en python, y mostrar ejemplos de cada caso, como por ejemplo, usar una lista para almacenar una secuencia de elementos de diferentes tipos de datos, o usar un array para almacenar una secuencia de elementos del mismo tipo de dato, etc.
#Inv 5.2  comprensiones anidadas, copy vs deepcopy Procesamiento de logs, etc.
#Realizar una investigacion sobre las comprensiones anidadas en python, copy vs deepcopy en python, y el procesamiento de logs en python, y mostrar ejemplos de cada caso.
#Ejercicio:
#5.1)Escriba un programa  que lea una lista de palabra 
#y ordene segun su logitud de menor a mayor, y luego imprima la lista ordenada.
#Si hay un sub conjunto de palabras con la misma longitud, ordene ese subconjunto alfabeticamente.
