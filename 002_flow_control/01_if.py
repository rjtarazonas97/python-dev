###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

print("\n Sentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")

edad = 16

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")

#Sentencia condicional else bifurcacion

edad = 15

if edad >= 18:
    print("Eres mayot de edad")
    print("Felicidades")
else:
    print("Eres menor de edad")

#Sentencia condicional ELIF

nota = 10 
if nota >= 9:
    print("Sobresasliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprovado")
else:
    print("No esta calificado")


#Condiciones multiples
## && -> and
## || -> or

edad = 25
tiene_carnet = True

#Un pueblo de Lima
if edad >= 18 and tiene_carnet: #and es = &&
    print("Puedes conducir")
else:
    print("Policia arrestelo")

#Un pueblo de Carabayllo
if edad >= 18 or tiene_carnet: #and es = &&
    print("Puedes conducir")
else:
    print("PAga al policia y te deja conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Hay que buscar chamba para crecer")


print("\n Anidar condicionales")
edad=20
tiene_dinero=True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")


# manera mas  facil

if edad < 18:
    print("No puede entrar a la disco")
elif tiene_dinero:
    print(" Puede ir a la discoteca")
else:
    print("Quedate en casa")

numero = 5
if numero: #True
    print("El numero no es cero")

numero = 0
if numero: #False
    print("Aqui no entrara nunca cero")

nombre = ""
if nombre:
    print("El nombre no es vacio")

numero = 3 #asignacion
el_el_tres = numero == 3 # comparacion

if el_el_tres:
    print("El numero es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# a = input("Ingresa el primero numero\n")
# b = input("ingresa el segundo numero\n")

# if a > b:
#     print(f"Si {a} es mayor que {b}")
# elif b > a:
#     print(f"Si {b} es mayor que {a}")
# else:
#     print("Los numero son iguales")

   
# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# num1= input("Ingresa el primer numero\n")
# num2= input("Ingresa el segundo numero\n")
# operacion= input("Ingresa el tipo de operacion (+, -, *, /) \n")


# if operacion == "+":
#     print(f"La suma es {num1} + {num2}")
# elif operacion == "-":
#     print(f"La resta es {num1} - {num2}")
# elif operacion == "*":
#     print(f"La multiplicacion es {num1} * {num2}")
# elif operacion == "/":
#     if num2 == 0:
#         print("El numero no se puede dividir entre 0")
#     else:
#         print(f"La division es {num1}/{num2} ")
# else:
#     print("Operacion no valida")



# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# anio = input("Ingrese el anio\n")

# if(anio % 4 == 0 and anio % 100 !=0)or anio % 400 == 0:
#     print(f"{anio} es un anio bisiesto")
# else:
#     print(f"{anio} no es un anio bisiesto")



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Ingrese la edad del nino\n"))

if edad >= 0 and edad <= 2:
    print("Es un bebe")
elif edad >= 3 and edad <= 12:
    print("Es un nino")
elif edad >= 13 and edad <= 17:
    print("Es un adolecente")
elif edad >= 18 and edad <= 64:
    print("Es un adulto")
else:
    print("Es un adulto mayor")