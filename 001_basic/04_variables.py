###
# 04 - variables
# Las variables sirvven para guardar datos en memoria
# Python es u n lenguaje de tipado dinamico y de tipado fuerte.
###

# Para asignar una variable
# solo hace falta hacer lo siguiente

my_name = "jesus"
print(my_name)

age = 27
print(age)

# age = 39
# print(age)


#Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion

name = "Jesus"
print(type(name))

name = 31
print(type(name))

#Tipado fuerte: Python no realiza conversiones de tipado automatico
#print(10 + "2")

print(f"Hola {my_name}, tengo {age} años")

#Desde la version 3.6 
#f-string (literal de cadena de formato) aca si pues agregar  a diferencia de esto #print(10 + "2")
print(f"Hola {my_name}, tengo {age + 4} años")



#No recomendada forma de asignar variables
name, age, city = "jesus", 27, "Lima"

#convenciones de variables
mi_nombre_de_varaible = "ok"
nombre = "ok"

MiNombreDeVariable = "ko" #PascalCase
minombredevariable = "ko" #todojunto

mi_nombre_de_varaible_123 = "ok"

# MI_CONSTANTE = 3.14 ... Python no tiene constantes UPPER_CASE -> constantes

MI_CONSTANTE = 2
print(MI_CONSTANTE)

# nombres no válidos de variables
# 123123_variable = "ko"
#mi-variable = "ko"
#mi variable = "ko"


#Palabras reservadas de Python
# True = False
# ['False', 'None', 'True', 'and', 'as', 'assert', # 'async', 'await', 'break', 'class', 'continue', 
# # 'def', 'del', 'elif', 'else', 'except', 'finally', 
# # 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
# # 'lambda', 'nonlocal' 'not', 'or', 'pass', 'raise', # 'return', 'try', 'while', 'with', 'yield']|