peliculas = {"anabel": "fast & furious",
            "karla": "demon night",
            "joaco": "cars"
            }

print(peliculas["anabel"])

for nombre, peli in peliculas.items():
    print("Nombre  mono: %s" % nombre)
    print("Nombre movie: %s" % peli)


num = 24 * 10
nombre = "Cookie"
utiles = ["mochila","libreta","lapiz"]
frutas = ["manzanda","pera","uva"]
dia_clases = {"nombre": nombre, "utiles": utiles, "frutas": frutas, "num":num}
print (dia_clases["frutas"])