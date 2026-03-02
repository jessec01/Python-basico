#diccionario 
#un diccionario es una estructura de datos que almacena pares de clave-valor, donde cada clave es unica y se utiliza para acceder a su valor correspondiente.
lista_vacia = [] #lista vacia
tupla_vacia = () #tupla vacia
diccionario_vacio = {} #diccionario vacio
#llave valor
diccionario_persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"} #diccionario con pares de clave-valor
#acceso a elementos de un diccionario
print(diccionario_persona["nombre"]) #acceso al valor de la clave "nombre"
print(diccionario_persona["edad"]) #acceso al valor de la clave "edad"
print(diccionario_persona["ciudad"]) #acceso al valor de la clave "ciudad"
#json 
json_persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"} #diccionario con pares de clave-valor en formato json
#practica de diccionario:
#dado un diccionario de personas, imprimir el nombre de la persona con la edad mayor
diccionario_personas = {"persona1": {"nombre": "Juan", "edad":
    30}, "persona2": {"nombre": "Maria", "edad": 25}, "persona3": {"nombre": "Pedro", "edad": 35}} #diccionario de personas con pares de clave-valor
persona_mayor = "" #inicializa la variable persona_mayor con una cadena vacia
edad_mayor = 0 #inicializa la variable edad_mayor con cero
for persona in diccionario_personas: #bucle for para recorrer el diccionario de personas
    if diccionario_personas[persona]["edad"] > edad_mayor: #condicion para verificar si la edad de la persona es mayor que la edad mayor actual
        edad_mayor = diccionario_personas[persona]["edad"] #actualiza la edad mayor con el nuevo valor
        persona_mayor = diccionario_personas[persona]["nombre"] #actualiza la persona mayor con el nuevo valor
print("La persona con la edad mayor es: ", persona_mayor) #imprime el nombre de la persona con la edad mayor
#Investigacion
#Inv. 7.0 Rendimiento de diccionarios vs listas
#Realizar una investigacion sobre el rendimiento de los diccionarios vs las listas en python, que es la diferencia en el tiempo de ejecucion y el uso de memoria entre los diccionarios y las listas, y mostrar ejemplos de cada caso, como por ejemplo, crear un diccionario y una lista con el mismo contenido y medir el tiempo de ejecucion y el uso de memoria de cada uno, etc.
#Ejercicio:
#Inv 7.1  get(), defaultdict, Counter
#Realizar una investigacion sobre las funciones get(), defaultdict y Counter en python, que son funciones que se utilizan para trabajar con diccionarios, y mostrar ejemplos de cada caso, como por ejemplo, usar get() para acceder a un valor de un diccionario sin generar un error si la clave no existe, usar defaultdict para crear un diccionario con un valor por defecto para las claves que no existen, y usar Counter para contar la frecuencia de los elementos de una lista o un diccionario, etc.
#7.1) Escriba un programa que lea un diccionario de palabras y sus definiciones, y permita al usuario buscar la definicion de una palabra ingresando su clave, e imprima la definicion correspondiente. Si la palabra no se encuentra en el diccionario, imprimir un mensaje de error indicando que la palabra no se encuentra en el diccionario.
