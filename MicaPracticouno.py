#Lista de números pares.
#Escribe un programa que solicite al usuario ingresar 10 números y luego imprima una lista con los números pares ingresados.
numerospares=[]
for i in range(10):
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        numerospares.append(numero)

print("Números pares ingresados:", numerospares)
