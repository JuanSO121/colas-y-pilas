# un centro meteorologico que necesita registrar diariamente los datos de sus distintas estaciones. 
# Tenga en cuenta los requerimentos: 
# a) por estacion meteorologia se debe conocer su pais de ubicacion, asi como coordenadas (latidud,longitud y altitud). 
# b) Las estaciones registran en distintas horas, la termperatura, presion, humedad y estado del clima (soleado, nublado, llovia, nevado). usando clases para los atributos
# c) se debe indicar el promedio de temperatura y humedad de todas las estaciones durante un mes especificado
# d)se deben buscar las estaciones meteorologicas que hayan registrado un estado de clima determinado.

import random
from tda_lista import Lista, insertar, barrido, buscar, eliminar

class Coordenadas:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
        
class EstacionMeteorologica:
    def __init__(self, pais,coordenadas):
        self.pais = pais
        self.coordenadas = coordenadas
        self.registros = []
        
    # comparar objetos de la clase EstacionMeteorologica
    def __lt__(self, siguiente):
        return self.coordenadas.altitud < siguiente.coordenadas.altitud

class RegistroMeteorologico:
    def __init__(self, temperatura, presion, humedad, estado_clima, fecha, hora):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.estado_clima = estado_clima
        self.fecha = fecha
        self.hora = hora

lista = Lista()

climas_posibles = ['soleado', 'nublado', 'lluvia', 'nevado']
paises = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Puerto Rico', 'República Dominicana', 'Uruguay', 'Venezuela']

# función para crear estaciones meteorológicas y registros aleatorios
def crearEstaciones(cant_estaciones):
    for i in range(cant_estaciones):
        pais = random.choice(paises)
        latitud = random.uniform(-90, 90)
        longitud = random.uniform(-180, 180)
        altitud = random.uniform(0, 5000)

        coordenadas = Coordenadas(latitud, longitud, altitud)
        estacion = EstacionMeteorologica(pais,coordenadas)
 
        for j in range(30):
            mesBuscar = random.randint(1, 12)
            fecha = f"{j+1}/{mesBuscar}/2023" 
            
            registro = RegistroMeteorologico(
                random.uniform(5, 35),
                random.uniform(900, 1100),
                random.uniform(0, 100),
                random.choice(climas_posibles),
                fecha,
                random.randint(0, 23)
            )
            estacion.registros.append(registro)
            
         # se inserta la estación en la lista
        insertar(lista, estacion)

# función para buscar estaciones meteorológicas que tengan registros con un clima específico
def buscarEstacionesPorClima(buscado):
    nodo = lista.inicio
    posicion = buscar(lista, nodo.info)
    ultima_estacion = None
    
    while posicion is not None:
        for registro in posicion.info.registros:
            if registro.estado_clima == buscado:
                if posicion.info != ultima_estacion:
                    print(f'La estación meteorológica en {posicion.info.pais} que registro el clima {buscado}, tiene las siguientes coordenadas: ')
                    print(f'Latitud: {posicion.info.coordenadas.latitud}°')
                    print(f'Longitud: {posicion.info.coordenadas.longitud}°')
                    print(f'Altitud: {posicion.info.coordenadas.altitud} m\n')
                    ultima_estacion = posicion.info
                
                print(f'Registro encontrado en la fecha {registro.fecha} en la hora {registro.hora} ')
                # Puedes almacenar todas las fechas en una lista y luego imprimirlas en una sola cadena:
                # fechas = [r.fecha for r in posicion.info.registros if r.estado_clima == buscado]
                # print(f'Fechas de registro: {", ".join(fechas)}')
                print()
                
        posicion = posicion.sig

    if ultima_estacion is None:
        print(f'No se encontraron estaciones meteorológicas que registraran un clima {buscado}.')


def promedio(mes):
    temperatura_total = 0
    humedad_total = 0
    cant_registros = 0

    nodo = lista.inicio

    while nodo is not None:
        for registro in nodo.info.registros:
            if registro.fecha.startswith(mes):
                temperatura_total += registro.temperatura
                humedad_total += registro.humedad
                cant_registros += 1
        nodo = nodo.sig

    if cant_registros > 0:
        temperatura_promedio = temperatura_total / cant_registros
        humedad_promedio = humedad_total / cant_registros
        print(f'El promedio de temperatura del mes {mes} es {temperatura_promedio:.2f}°C.')
        print(f'El promedio de humedad del mes {mes} es {humedad_promedio:.2f}%.')
    else:
        print(f'No se encontraron registros para el mes {mes}.')


cant_estaciones = int(input("\nCuantas estaciones desea evaluar? "))
crearEstaciones(cant_estaciones)
        
while True:
    print("\n Que desea realizar?: ")
    print("a) Mostrar estaciones")
    print("b) Hallar promedio de temperatura y humedad de todas las estaciones")
    print("c) Buscar estaciones por clima")
    print("d) Salir del programa")

    opcion = input()
    if opcion == 'a':
        barrido(lista)
        
    elif opcion == 'b':
        mes = input('Ingrese el mes para calcular el promedio de temperatura y humedad (1 - 12): ')
        if mes.isnumeric() and 1 <= int(mes) <= 12:
            promedio(mes)
        else:
            print('Mes inválido. Intente nuevamente.')
        
    elif opcion == 'c':
        buscado = input('\nIngrese un clima a buscar (soleado, nublado, lluvia, nevado): ')
        buscarEstacionesPorClima(buscado)
         
    elif opcion == 'd':
        print("ha finalizado el programa")
        break

    else:
        print("Opción inválida, intente nuevamente.\n")
