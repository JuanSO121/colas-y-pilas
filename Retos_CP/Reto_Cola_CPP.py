# Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro), que resuelva las siguientes actividades:
# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son los siguientes: I. automóviles (tarifa $47); II. camionetas (tarifa $59); III. camiones (tarifa $71); IV. colectivos (tarifa $64).
# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

# tomar el tamañpo de cada cabina para que la atencion atienda a todas
from TDA_Cola import Cola, arribo, atencion, cola_vacia, tamaño, en_frente, barrido_mover_final, mover_al_final,barrido
import random
tipos_vehiculos = ['automóvil', 'camioneta', 'camión', 'colectivo', 'moto']

# hacer referencia directamente al precio del vehiculo
tarifas_vehiculos = {
    'automóvil': 47,
    'camioneta': 59,
    'camión': 71,
    'colectivo': 64,
    'moto': 35
}


listaContador = [0 for _ in range(len(tipos_vehiculos))]
total = [0 for _ in range(len(tipos_vehiculos))]

cabina1 = Cola()
cabina2 = Cola()
cabina3 = Cola()

# Crear diccionario con los contadores por tipo de vehículo y por cabina
vehiculos_por_cabina_y_tipo = {cabina1: {tipo: 0 for tipo in tipos_vehiculos}, 
                               cabina2: {tipo: 0 for tipo in tipos_vehiculos}, 
                               cabina3: {tipo: 0 for tipo in tipos_vehiculos}}

# Función para agregar un vehículo a una cabina de cobro
def agregar_vehiculo():
    tipo_vehiculo = random.choice(tipos_vehiculos)
    tarifa_vehiculo = tarifas_vehiculos[tipo_vehiculo]
    vehiculo = {
        'tipo': tipo_vehiculo,
        'tarifa': tarifa_vehiculo,
        'tiempo_llegada': random.randint(0, 30),
        'cabina_asignada': None,
    }
    
    precio = tarifa_vehiculo
    listaContador[tipos_vehiculos.index(tipo_vehiculo)] += 1
    total[tipos_vehiculos.index(tipo_vehiculo)] += precio
    cabina = random.choice([cabina1, cabina2, cabina3])
    arribo(cabina, vehiculo)
    

    # Incrementar el contador correspondiente en el diccionario
    vehiculos_por_cabina_y_tipo[cabina][tipo_vehiculo] += 1
       
def atender_cabinas():
    # Verificar si hay algún vehículo en el frente de cada cabina
    for cabina in [cabina1, cabina2, cabina3]:
        while not cola_vacia(cabina):
            vehiculo = en_frente(cabina)
            tipo_vehiculo = vehiculo['tipo']
            tarifa_vehiculo = vehiculo['tarifa']
            cabina_asignada = vehiculo['cabina_asignada']
            precio = tarifa_vehiculo
            total[tipos_vehiculos.index(tipo_vehiculo)] += precio
            print(f"Vehículo {tipo_vehiculo} atendido en cabina {cabina_asignada}. Precio de la tarifa: {precio}")
            atencion(cabina)

            # Incrementar el contador correspondiente en el diccionario
            vehiculos_por_cabina_y_tipo[cabina][tipo_vehiculo] += 1


def siguiente_en_cola(cola):
    # Si la cola está vacía, devolver None
    if cola_vacia(cola):
        return None
    # Obtener el primer elemento de la cola
    vehiculo = en_frente(cola)
    # Quitar el elemento de la cola
    atencion(cola)
    # Devolver el elemento y agregarlo al final de la cola
    arribo(cola, vehiculo)
    return vehiculo


# Agregar 30 vehículos de manera aleatoria a las cabinas de cobro
for i in range(30):
    agregar_vehiculo()
    

while True:
    print("\n Seleccione una opción:")
    print("a) realizar la atención de las cabinas")
    print("b) Determinar la cabina que recaudó la mayor cantidad de pesos")
    print("c) Mostrar el número de vehículos que pasaron por las cabinas de peaje")
    print("d) Salir del programa")

    opcion = input()
          
    if opcion == 'a':
        for cabina in [cabina1, cabina2, cabina3]:
            vehiculo = siguiente_en_cola(cabina)
            if vehiculo is not None:
                tipo_vehiculo = vehiculo['tipo']
                tarifa_vehiculo = vehiculo['tarifa']
                precio = tarifa_vehiculo
                listaContador[tipos_vehiculos.index(tipo_vehiculo)] -= 1
                total[tipos_vehiculos.index(tipo_vehiculo)] += precio
                vehiculo['cabina_asignada'] = cabina
                # Decrementar el contador correspondiente en el diccionario
                vehiculos_por_cabina_y_tipo[cabina][tipo_vehiculo] -= 1
                print(f"Vehículo {tipo_vehiculo} atendido en cabina {cabina}. Precio de la tarifa: {tarifa_vehiculo}")

    elif opcion == 'b':
        # obtener la cantidad de vehículos en cada cola
        cant_cabina1 = tamaño(cabina1)
        cant_cabina2 = tamaño(cabina2)
        cant_cabina3 = tamaño(cabina3)

        # calcular la recaudación de cada cabina
        recaudacion_cabina1 = total[0] * cant_cabina1
        recaudacion_cabina2 = total[1] * cant_cabina2
        recaudacion_cabina3 = total[2] * cant_cabina3

        # guardar las recaudaciones en una lista
        recaudaciones = [recaudacion_cabina1, recaudacion_cabina2, recaudacion_cabina3]

        # encontrar la cabina con mayor recaudación
        cabina_ganadora = recaudaciones.index(max(recaudaciones)) + 1

        # imprimir las recaudaciones y la cabina ganadora
        print("Recaudación de la cabina 1:", recaudacion_cabina1)
        print("Recaudación de la cabina 2:", recaudacion_cabina2)
        print("Recaudación de la cabina 3:", recaudacion_cabina3)
        print(f"La cabina que recaudó la mayor cantidad de pesos fue la número {cabina_ganadora}")
            
    elif opcion == 'c':
            print("Vehículos que pasaron por cada cabina:")
            for cabina in [cabina1, cabina2, cabina3]:
                num_vehiculos = tamaño(cabina)
                print(f"{cabina}: {num_vehiculos} vehículos")
                for tipo_vehiculo in tipos_vehiculos:
                    num_vehiculos_tipo = vehiculos_por_cabina_y_tipo[cabina][tipo_vehiculo]
                    print(f"\t{tipo_vehiculo}: {num_vehiculos_tipo}")
            
    elif opcion == 'd':
        print("ha finalizado el programa")
        break

    else:
        print("Opción inválida, intente nuevamente.")