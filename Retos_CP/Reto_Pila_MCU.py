"""Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

c. determinar en cuantas películas participó la Viuda Negra (Black Widow);

d. mostrar todos los personajes cuyos nombre empiezan con C, D y G."""

# crear auxiliar para rellenar la pila

from TDA_Pila import Pila, apilar, desapilar, pila_vacia,barrido

superheroes = {
    'Thor': 5,
    'Captain America': 6,
    'Hulk': 3,
    'Black Widow': 6,
    'Hawkeye': 4,
    'Ant-Man': 2,
    'Spider-Man': 2,
    'Doctor Strange': 2,
    'Black Panther': 2,
    'Captain Marvel': 1,
    'Rocket Raccoon': 4,
    'Groot': 4
}

def rellenar_pila():
    while not pila_vacia(pila_mcu):
        desapilar(pila_mcu)
    agregar_superheroes()

pila_mcu = Pila()

# Función para apilar los superhéroes
def agregar_superheroes():
    for nombre, peliculas in superheroes.items():
        apilar(pila_mcu, (nombre, peliculas))

# Llamamos a la función para cargar los superhéroes en la pila
print("Apilando los superhéroes...")
agregar_superheroes()
print("¡Superhéroes apilados con éxito!")
print()

print("¿Qué actividad desea realizar?")
print("1. En qué posición se encuentran Rocket Raccoon y Groot?")
print("2. Cuáles son los personajes que participaron en más de 5 películas?")
print("3. En que peliculas participó la Viuda Negra (Black Widow)?")
print("4. Cuáles son los personajes cuyo nombre empieza con C, D y G?")
print("5. Salir")

opcion = input("Elija una opción: ")

while opcion != "5":
    
    if opcion == "1":
        posicion = 1
        personajes_encontrados = 0
        while not pila_vacia(pila_mcu) and personajes_encontrados < 2:
            personaje = desapilar(pila_mcu)
            if personaje[0] in ("Rocket Raccoon", "Groot"):
                print(f"{personaje[0]} se encuentra en la posición {posicion}")
                personajes_encontrados += 1
            posicion += 1
            if personajes_encontrados == 0:
                print("No se encontraron personajes")

    elif opcion == "2":
        print("\nPersonajes que participaron en más de 5 películas:")
        while not pila_vacia(pila_mcu):
            personaje = desapilar(pila_mcu)
            if personaje[1] > 5:
                print(f"- {personaje[0]} ({personaje[1]} películas)")
                
    if opcion == "3":
        rellenar_pila()
        while not pila_vacia(pila_mcu):
            personaje = desapilar(pila_mcu)
            if personaje[0] == "Black Widow":
                print(f"\nLa Viuda Negra (Black Widow) participó en {personaje[1]} películas")
                break
            
    elif opcion == "4":
        rellenar_pila()
        personajes_cdg = []
        while not pila_vacia(pila_mcu):
            personaje = desapilar(pila_mcu)
            if personaje[0][0] in ("C", "D", "G"):
                personajes_cdg.append(personaje[0])
        print("Los personajes cuyos nombres empiezan con C, D o G son:")
        for personaje in personajes_cdg:
            print(f"- {personaje}")
    opcion = input("\nIngrese otra opción o 5 para salir: ")
print("¡Gracias por utilizar este programa!")
