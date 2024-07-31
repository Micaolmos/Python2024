#Contar vocales en una frase.
#Escribe un programa que solicite al usuario ingresar una frase y luego cuente e imprima la cantidad de vocales (a, e, i, o, u) que contiene la frase.
frase = input("Ingresa una frase: ")
vocales = "aeiouAEIOU"
cantidadVocales = sum( 1 for i in frase if i in vocales)
print(f"Número de vocales en la frase: {cantidadVocales}")