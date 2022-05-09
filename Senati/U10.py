# 1.	Realizar un programa para saber si eres un adulto.

edad = int(input('Ingrese una edad: '))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
# -----------------------------------------------------------------------------
# 2.	Crear un programa, donde ingreses tu edad e
# imprimir si eres mayor de edad o menor de edad.

edad = int(input('Ingrese una edad: '))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# -----------------------------------------------------------------------------
# 3.	Escribir un programa que compare 2 números e
# imprime si son iguales o no son iguales.

x1 = int(input("Ingrese primer numero: "))
x2 = int(input("Ingrese segundo numero: "))

if x1 == x2:
    print("Son numeros iguales")
else:
    print("No son numeros iguales")

# -----------------------------------------------------------------------------------
# 4.	Realizar un programa para saber etapas de la vida y acorde a tu
#       edad imprimir lo siguiente:
#
# a)	Niñez (6-11)
# b)	Adolescencia (12-18)
# c)	Juventud (18-26)
# d)	Adultez (27-59)
# e)	Vejez (60 a más)

edad = int(input("Ingrese su edad: "))

if edad >= 6 and edad <= 11:
    etapa = "niñez"
elif edad >= 12 and edad <= 18:
    etapa = "Adolescencia"
elif edad > 18 and edad <= 26:
    etapa = "Juventud"
elif edad >= 27 and edad <= 59:
    etapa = "Adultez"
elif edad >= 60:
    etapa = "Vejez"
else:
    etapa = "Dato Incorrecto no Existe"

print("Usted se encuentra en la etapa de ", etapa)

# ---------------------------------------------------------------------------------------
# 5.	Realizar un ejemplo para imprimir el mes del año de acuerdo con el
# número ingresado, si se ingresa un número fuera del rango imprimir debe
# mostrar el mensaje “valor invalido”, ejemplo:
# a)	Número 12 es igual a diciembre.

años = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio",
        8: "Agosto", 9: "Setiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

num = int(input("Ingrese un numero: "))

if num == 1:
    print(años[num])
elif num == 2:
    print(años[num])
elif num == 3:
    print(años[num])
elif num == 4:
    print(años[num])
elif num == 5:
    print(años[num])
elif num == 6:
    print(años[num])
elif num == 7:
    print(años[num])
elif num == 8:
    print(años[num])
elif num == 9:
    print(años[num])
elif num == 10:
    print(años[num])
elif num == 11:
    print(años[num])
elif num == 12:
    print(años[num])
else:
    print("Error")

# ---------------------------------------------------------------------------------------

# 6.	Crear un programa para verificar el usuario y contraseña, si ingreso correctamente
# los datos imprimir “Bienvenido” en caso contrario “Inténtelo de nuevo".


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


# si se verifica usuario y contraseña
# elegido = int(input("""¿Desea cambiar la contraseña?
#
#                     Pulse 1 si desea cambiarla.
#
#                     Pulse 2 si desea salir.
#
#                     Opción: """))
# if elegido == 1:
#     usuario = input("Ingrese nombre de usuario: ")
#     if login.get(usuario):
#         password = input("Ingrese la nueva clave: ")
#         login[usuario] = password  # acá cambio el valor de la clave, pero es virtual, al reiniciar volverá la original
# elif elegido == 2:
#     print("Programa terminado ")
#     sys.exit()

# ---------------------------------------------------------------------------------------------
# 7.	Crear un programa que permita saber si un año es bisiesto,
# si es bisiesto imprimir “Este año es bisiesto” o en caso contrario
# "No es un año bisiesto".
# observacion: Matemáticamente podemos saber si un año es bisiesto si
#              este es múltiplo de 4. Si además es múltiplo de 100 no será
#              bisiesto (ten en cuenta que 100 es múltiplo de 4 y por tanto
#              cualquier número que sea múltiplo de 100 también es múltiplo de 4)
#              a no ser que sea múltiplo de 400, que sí será bisiesto.

# if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
# 	print("Es bisiesto")
# else:
# 	print("No es bisiesto")

def es_bisiesto(x):
    return not x % 4 and (x % 100 or not x % 400)


año = int(input("Ingrese el año: "))

if es_bisiesto(año):
    print('El año ' + str(año) + ' es Bisiesto', end=' ')
else:
    print('No es bisiesto')

# --------------------------------------------------------------------------------------------
# 8.	Realizar un programa que permita saber el día de acuerdo con el número ingresado.
años = {1: "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sabado", 7: "Domingo"}

num = int(input("Ingrese un numero: "))

if num == 1:
    print(años[num])
elif num == 2:
    print(años[num])
elif num == 3:
    print(años[num])
elif num == 4:
    print(años[num])
elif num == 5:
    print(años[num])
elif num == 6:
    print(años[num])
elif num == 7:
    print(años[num])
else:
    print("Error")

# --------------------------------------------------------------------------------------------
# 9.	Ingresar dos números e imprimir cuál de los dos es mayor.
x=int(input("ingresar primer numero: "))
y=int(input("Ingresar segundo numero: "))

if x > y:
    mayor=x
else:
    mayor=y

print('El numero mayor es ',mayor)

#--------------------------------------------------------------------------------------------
#10.	Ingresar un número entero y mostrar si es par o impar.

num=int(input("Ingresar un numero entero: "))

if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")