###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

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