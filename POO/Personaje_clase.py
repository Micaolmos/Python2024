import random
class Personaje:
    #atributo de clase
  estado = True #vivo
  vida = 100 #cantidad de vida
   #costructor / atributo de instancia
def __int__(self, nombre, altura, velocidad, resistencia, fuerza):  
      self.nombre = nombre
      self.altura = altura
      self.velocidad = velocidad
      self.resistencia = resistencia
      self.fuerza = fuerza
      self.estado = Personaje.estado
      self.vida = Personaje.vida

def atacar(self, otro_personaje):
    if self.estado: #si estoy vivo es lo mismo que self
       danio = self.fuerza - (otro_personaje.resistencia)
       print(f"{self.nombre} ataca a {otro_personaje.nombre} causado {danio} de daño:")
       otro_personaje.recibir_dano(danio)#llamando al metodo
    else:
      print(f"{self.nombre}muerto")
#cantidad va a tomar el valor del Danio

def recibir_danio(self, cantidad):
  #Cantidad = Daño recibido 
    if self.estado:
        self.vida = self.vida  -  cantidad #self.vida = cantida
        print(f"{self.nombre} recibe {cantidad} de danio. Vida resta")
        if self.vida <=0: #Si vida es igual o menor a 0 vida es igual a 0 para que no nos de numeros negativos
          self.vida = 0
          print(f"{self.nombre} ya muerto")
    else:
       print(f"{self.nombre} ya muerto")
#Muestra cuando esta muerto y la cantidad de vida que pierde
def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura} cm")
        print(f"Velocidad: {self.velocidad}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")

nuevo_personaje = Personaje()

#Muestra en la pantalla la información del personaje.