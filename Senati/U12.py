# Definiendo funciones
#
# 1.	Crear una función que imprima “Hola mundo”
def my_function():
    print("Hola Mundo!!!")
my_function()

# 2.	Crear una función que imprima la suma de dos números.

def operacion_suma(x,y):
    return x+y
x=int(input("Ingrese primero numero: "))
y=int(input("Ingrese segundo numero: "))
print("La suma de los dos numeros es: "+str(operacion_suma(x,y)))

# 3.	Crear una función que permita saber qué número es mayor.

    cant=int(input("Ingresar cantidad de numeros: "))
    lista_num=[]
    for x in range(cant):
        x=int(input(f"Ingrese num{x+1}:"))
        lista_num.append(x)
   def mayor(lista_num):
       max=lista_num[0]
       for x in lista_num:
           if x>max:
               max=x
       return max

print("El numero mayor es: ", mayor(lista_num))

# 4.	Crear una función que permita verificar que un número de
#       teléfono tenga 9 dígitos.



# 5.	Cree una función llamada saludo, que reciba como parámetro
#       el nombre y apellido e imprime: “Hola me llamo NOMBRE y tengo la edad 38.

# 6.	Realizar una función que halle el área del triángulo.

# 7.	Realizar una función que halle el área del cuadrado.

# 8.	Crear una función que reciba como parámetro 2 años e imprimir
#       la diferencia de años.

# 9.	Crear una función que reciba como parámetro un número entero e
#       imprima si es par o impar.

# 10.	Crear una función que permita saber el promedio de dos números.

