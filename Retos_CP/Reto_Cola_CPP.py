# Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro), que resuelva las siguientes actividades:
# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son los siguientes: I. automóviles (tarifa $47); II. camionetas (tarifa $59); III. camiones (tarifa $71); IV. colectivos (tarifa $64).
# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

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
    
def atender_vehiculo(cabina):
    vehiculos_atendidos = []
    while not cola_vacia(cabina):
        vehiculo = en_frente(cabina)
        tipo_vehiculo = vehiculo['tipo']
        tarifa_vehiculo = vehiculo['tarifa']
        atencion(cabina)
        print(f"Cabina {cabina}: Cobrando ${tarifa_vehiculo} por vehículo de tipo {tipo_vehiculo}")
        vehiculos_atendidos.append(vehiculo)
    print(f"Cabina {cabina}: No hay vehículos en espera")
    total_recaudado_cabina = sum([vehiculo['tarifa'] for vehiculo in vehiculos_atendidos])
    cantidad_vehiculos_atendidos = len(vehiculos_atendidos)
    print(f"Cabina {cabina}: Total recaudado ${total_recaudado_cabina} por {cantidad_vehiculos_atendidos} vehículos")




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
                # Atender los vehículos en las cabinas de cobro
        for cabina in [cabina1, cabina2, cabina3]:
            atender_vehiculo(cabina)
            total_recaudado_cabina = sum([vehiculo['tarifa'] for vehiculo in barrido(cabina)])
            print(f"Cabina {cabina}: Total recaudado ${total_recaudado_cabina}")
            
        print("Todas las cabinas han terminado de atender vehículos.")

        
    elif opcion == 'b':
        print("Vehículos que pasaron por cada cabina:")
        for cabina in [cabina1, cabina2, cabina3]:
            num_vehiculos = tamaño(cabina)
            print(f"{cabina}: {num_vehiculos} vehículos")
            for tipo_vehiculo in tipos_vehiculos:
                num_vehiculos_tipo = vehiculos_por_cabina_y_tipo[cabina][tipo_vehiculo]
                print(f"\t{tipo_vehiculo}: {num_vehiculos_tipo}")
    
    elif opcion == 'c':
        print("Ingresos en la cabina 1:", total[0] * listaContador[0])
        print("Ingresos en la cabina 2:", total[1] * listaContador[1])
        print("Ingresos en la cabina 3:", total[2] * listaContador[2])
    
        # usar atencion y barrido
        recaudacion_cabina1 = total[0] * listaContador[0]
        recaudacion_cabina2 = total[1] * listaContador[1]
        recaudacion_cabina3 = total[2] * listaContador[2]
        recaudaciones = [recaudacion_cabina1, recaudacion_cabina2, recaudacion_cabina3]
        mayor_recaudacion = max(recaudaciones)
        cabina_ganadora = recaudaciones.index(mayor_recaudacion) + 1
        print(f"La cabina que recaudó la mayor cantidad de pesos fue la número {cabina_ganadora}")
      
    elif opcion == 'd':
        print("ha finalizado el programa")
        break

    else:
        print("Opción inválida, intente nuevamente.")
