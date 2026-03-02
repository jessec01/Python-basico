#fstring
nombre_usuario="Juan"
apellido_usuario="Perez"
nombre_completo_viejo= nombre_usuario + " " + apellido_usuario #concatenacion de cadenas de texto usando el operador +
nombre_completo= f"{nombre_usuario} {apellido_usuario}" #fstring para concatenar el nombre y el apellido del usuario
nombre_usuario = input("Ingrese su nombre: ") #entrada de datos por teclado
edad_usuario = int(input("Ingrese su edad: ")) #entrada de datos por teclado y conversion a int
price_usuario = float(input("Ingrese el precio: ")) #entrada de datos por teclado
numero= 10
#salida de datos usando fstring
print(f"Hola, {numero}") #salida de datos por pantalla usando fstring
print(f"Tu edad es: {edad_usuario}") #salida de datos por pantalla usando
print(f"El precio es: {price_usuario}") #salida de datos por pantalla usando fstring
#str.format(), regex básico (re module) Parser de textos 
#uso de str.format() para imprimir un mensaje con variables
print("Hola, {}".format(nombre_usuario)) #salida de datos por pantalla usando str.format()
#printf("%d", numero) #salida de datos por pantalla usando printf de c, no funciona en python
print("Tu edad es: {}".format(edad_usuario)) #salida de datos por pantalla usando str.format()
print("El precio es: {}".format(price_usuario)) #salida de datos
#salida de datos por pantalla usando str.format()
#uso de regex para validar una direccion de correo electronico
correo_electronico = input("Ingrese su correo electronico: ") #entrada de datos por teclado
#regex para validar una direccion de correo electronico
#Investigacion
#Inv 8.0 regex avanzado
#Realizar una investigacion sobre el uso avanzado de regex en python, como por ejemplo, el uso de grupos de captura, el uso de metacaracteres, el uso de funciones de regex, etc. y mostrar ejemplos de su uso en diferentes situaciones, como por ejemplo, validar una direccion de correo electronico, validar un numero de telefono, validar una fecha, etc. 
#Proyecto:
#Reaizar un programa que registre el nombre, la edad, el correo electronico y el numero de telefono de un usuario, y valide cada uno de estos datos usando regex, y luego imprima los datos validados en pantalla usando fstring.

#Condiciones: 
# Utilizar todo lo que se ha aprendido en las clases anteriores, como por ejemplo, condiciones, bucles, funciones, etc. para validar los datos ingresados por el usuario y para imprimir los resultados en pantalla.
#Usar alguna estructura de datos para almacenar los datos del usuario, como por ejemplo, una tupla, una lista, un diccionario.
#separar el codigo en funciones para cada tarea. 