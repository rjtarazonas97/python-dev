###
# 05 - Entrada de usuario (input()) – Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

nombre = input("Hola como te llamas?\n")

print(f"Hola {nombre}, encantado de conocerte")

age = input("Cuantos años tienes?")
age = int(age)
print(f"Tienes {age} años")


print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives?\n").split() #el split recupera la cadena de texto y los separa

print(f"Vives en {country} y {city}")
