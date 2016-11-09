def hola(nombre="Mundo"):
    print("Hola",nombre)

hola("Cookie")
hola()

class animal:
    def __init__(self, patas=4, tipo="pequeño"):
        self.patas=patas
        self.tipo=tipo
class perro(animal):
    def __init__(self, nombre = "Oddie", raza = "Jack"):
        self.nombre = nombre
        self.raza = raza
         #referencia a clase padre
#    def saludo(self):
#        return "Te saluda %s" % self.nombre

perrito = perro(nombre="Lucas", raza="jack")
perrito_hanz = perro()
print(perrito.nombre)
print(perrito.raza)
#print(perrito.tipo)
#print(perrito.patas)
#perrito.saludo
print(perrito_hanz.nombre)
print(perrito_hanz.raza)
#perrito_hanz.saludo