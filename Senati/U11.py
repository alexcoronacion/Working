# 1.	Crear un programa que imprima los números del 1 al 100.

for i in range(1,101):
    print(i)

# 2.	Crear un programa que imprima los números pares menores que 50.
for p in range(0,51,2):
    print(p)

# 3.	Realizar un programa que imprima los 20 primero números impares.
for imp in range(1,41,2):
    print(imp)

# 4.	Crear un programa que pida un número entero e imprimirlo, si no
#       ingresa deberá preguntar otra vez por el número entero hasta que ingrese un número positivo.



# 5.	Imprimir la tabla del 1 al 12 con bucles.

tabla_desde = 1 #tablas del 1...
tabla_hasta = 12 #...al 12
desde = 1 #multiplicaciones desde el 1...
hasta = 12 #...hasta el 12

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:') #mostramos una cabecera para cada tabla
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print() #línea en blanco al final de cada tabla

# 6.	Realizar un programa para verificar la contraseña, el usuario solo tendrá 3 intentos,
#       si pasa los intentos imprimir “Sobrepaso todos sus intentos”
import sys  # importando la libreria sys para terminar el script cuando quiera

login = {"Yazmin": "123", "Christian": "123", "Rodrigo": "123", "Gabriel": "123", "Dante": "123", "Adrian": "123"}

intentos = 0

while intentos < 3:
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if login.get(
            usuario) == password:  # con get se busca la clave del diccionario y se compara el valor con la clave(password) ingresada
        print("Bienvenido ", usuario)
        break
    else:
        print("El nombre de usuario o la contraseña son incorrectos")
    intentos += 1

if intentos == 3:
    print("Ha llegado al limite de intentos")
    sys.exit()

# 7.	Crear una lista que almacene edades.

cant=int(input("Ingrese la cantidad de edades: "))
lista=[]
for x in range(cant):
    x=int(input(f"edad {x+1}: "))
    lista.append(x)


print(lista)

# 8.	Con la lista anterior contar cuantos son mayores de edad.

cant=int(input("Ingrese la cantidad de edades: "))
lista=[]
cont=0
for x in range(cant):
    x=int(input(f"edad {x+1}: "))
    if x>18:
        cont+=1

    lista.append(x)

print("La cantidad de mayores de edad son: ",cont)

# 9.	Realizar un programa para contar cuantas letras tiene tu nombre.

# 10.	Crear un programa para una empresa, que pida la cantidad de clientes y luego las almacene
#       en un arreglo.
