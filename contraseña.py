contraseña = input("Ingrese su contraseña: ")
listaContrasena = []

for i in contraseña:

 print("*", end="") 
 listaContrasena.append(i)

print() 
print(listaContrasena) 
listaContrasena.pop(2)
print(listaContrasena)