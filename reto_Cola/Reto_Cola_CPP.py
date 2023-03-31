# Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro), que resuelva las siguientes actividades:
# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son los siguientes: I. automóviles (tarifa $47); II. camionetas (tarifa $59); III. camiones (tarifa $71); IV. colectivos (tarifa $64).
# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

from TDA_Cola import Cola, arribo, atencion, cola_vacia, tamaño, en_frente, barrido_mover_final, mover_al_final
import random

tipos_vehiculos = ['automóvil', 'camioneta', 'camión', 'colectivo', 'moto']
tarifas_vehiculos = [47, 59, 71, 64, 35]
listaContador = [0 for _ in range(len(tipos_vehiculos))]
total = [0 for _ in range(len(tipos_vehiculos))]

cabina1 = Cola()
cabina2 = Cola()
cabina3 = Cola()

# Función para agregar un vehículo a una cabina de cobro
def agregar_vehiculo():
    tipo_vehiculo = random.choice(tipos_vehiculos)
    tarifa_vehiculo = tarifas_vehiculos[tipos_vehiculos.index(tipo_vehiculo)]
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


# Agregar 30 vehículos de manera aleatoria a las cabinas de cobro
for i in range(30):
    agregar_vehiculo()

while True:
    print("\n Seleccione una opción:")
    print("a) Mostrar el número de vehículos en cada cabina")
    print("b) Mostrar la cantidad total de ingresos en cada cabina")
    print("c) Determinar la cabina que recaudó la mayor cantidad de pesos")
    print("d) Mostrar el número de vehículos de cada tipo que pasaron por las cabinas de peaje")
    print("e) Salir del programa")

    opcion = input()

    if opcion == 'a':
        print("Vehículos en la cabina 1:", tamaño(cabina1))
        print("Vehículos en la cabina 2:", tamaño(cabina2))
        print("Vehículos en la cabina 3:", tamaño(cabina3))
        
    elif opcion == 'b':
        print("Ingresos en la cabina 1:", total[0] * listaContador[0])
        print("Ingresos en la cabina 2:", total[1] * listaContador[1])
        print("Ingresos en la cabina 3:", total[2] * listaContador[2])
        
    elif opcion == 'c':
        recaudacion_cabina1 = total[0] * listaContador[0]
        recaudacion_cabina2 = total[1] * listaContador[1]
        recaudacion_cabina3 = total[2] * listaContador[2]
        recaudaciones = [recaudacion_cabina1, recaudacion_cabina2, recaudacion_cabina3]
        mayor_recaudacion = max(recaudaciones)
        cabina_ganadora = recaudaciones.index(mayor_recaudacion) + 1
        print(f"La cabina que recaudó la mayor cantidad de pesos fue la número {cabina_ganadora}")
        
    elif opcion == 'd':
        for i in range(len(tipos_vehiculos)):
            print(f"Número de vehículos de tipo {tipos_vehiculos[i]}: {listaContador[i]}")
            
    elif opcion == 'e':
        break
    
    else:
        print("Opción inválida, intente nuevamente.")
