"""Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

c. determinar en cuantas películas participó la Viuda Negra (Black Widow);

d. mostrar todos los personajes cuyos nombre empiezan con C, D y G."""


from collections import deque

# se crea la pila con los personajes de MCU

pila_mcu = deque([

    ('Thor', 4),
    ('Groot', 5),
    ('Hulk', 2),
    ('Black Widow', 6),
    ('Doctor Strange', 2),
    ('Ant-Man', 2),
    ('Thanos', 6),
    ('Spider-Man', 2),
    ('Rocket Raccoon', 4),
    ('Iron Man', 3),
    ('Black Panther', 2),
    ('Captain Marvel', 1),
    ('Captain America', 6)

])

#Determina la posición de Rocket Raccoon y Groot en la pila mcu

def posicion_rocket_y_groot(pila):

    rocket_pos = None
    groot_pos = None
    
    for i, personaje in enumerate(pila):
        if personaje[0] == 'Rocket Raccoon':
            rocket_pos = i+1
        elif personaje[0] == 'Groot':
            groot_pos = i+1
        if rocket_pos is not None and groot_pos is not None:
            break
    return rocket_pos, groot_pos

#Personajes en mas de 5 peliculas

def personajes_mas_de_5_peli(pila):
    personajes = []
    peliculas_por_personaje = {}
    for personaje in pila:
        if personaje[1] > 5:
            personajes.append(personaje[0])
            peliculas_por_personaje[personaje[0]] = personaje[1]
    return personajes, peliculas_por_personaje

personajes, peliculas_por_personaje = personajes_mas_de_5_peli(pila_mcu)



# Total de peliculas de la viuda negra (Black Widow)

def tot_peli_viuda_negra(pila):
    
    """Determina en cuantas películas participó la Viuda Negra"""
    
    for personaje in pila:
        if personaje[0] == 'Black Widow':
            return personaje[1]


# Personajes con las iniciales C, D y G

def personajes_con_iniciales(pila, iniciales):
    
    personajes = []
    for personaje in pila:
        if personaje[0][0] in iniciales:
            personajes.append(personaje[0])
    return personajes


# Mostrar resultados en la consola
def mostrar_menu(opciones):
    print('Marvel Cinematic Universe (MCU)')
    print('--------------------------------------', '\n')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('\n Digite la opción que desee: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

# Menú 

def menu_principal():
    opciones = {
        '1': ('¿En qué posición se encuentran Rocket Raccoon y Groot?', accion1),
        '2': ('¿Cuáles son los personajes que participaron en más de 5 películas?', accion2),
        '3': ('¿En que peliculas participó la Viuda Negra?', accion3),
        '4': ('¿Cuáles son los personajes cuyo nombre empieza con C, D y G?', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    print("\n La posición de Rocket Raccoon y Groot es:", posicion_rocket_y_groot(pila_mcu), "\n", "\n")


def accion2():
    print("\n Los personajes que participaron en más de 5 películas son:", personajes_mas_de_5_peli(pila_mcu), "\n", "\n")


def accion3():
    print("\n La Viuda Negra (Black Widow) participó en", tot_peli_viuda_negra(pila_mcu), "películas", "\n", "\n")

def accion4():
    print("\n Los personajes cuyo nombre empieza con C, D y G son:", personajes_con_iniciales(pila_mcu, ['C', 'D', 'G']), "\n", "\n")

def salir():
    print('\n Saliendo')

if __name__ == '__main__':
    menu_principal()