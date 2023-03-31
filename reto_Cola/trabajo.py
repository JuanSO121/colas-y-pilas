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
    if tipo_vehiculo in tipos_vehiculos:
        tarifa_vehiculo = tarifas_vehiculos[tipos_vehiculos.index(tipo_vehiculo)]
        vehiculo = {
            'tipo': tipo_vehiculo,
            'tarifa': tarifa_vehiculo,
            'tiempo_llegada': random.randint(0, 30),
            'cabina_asignada': None,
        }
        precio = tarifas_vehiculos[tipos_vehiculos.index(tipo_vehiculo)]
        listaContador[tipos_vehiculos.index(tipo_vehiculo)] += 1
        total[tipos_vehiculos.index(tipo_vehiculo)] += precio
        cabina = random.choice([cabina1, cabina2, cabina3])
        arribo(cabina, vehiculo)
    else:
        agregar_vehiculo() # Si el tipo de vehículo no está en la lista, se vuelve a intentar agregar otro vehículo

# Agregar 30 vehículos de manera aleatoria a las cabinas de cobro
for i in range(30):
    agregar_vehiculo()

# Realizar la atención de las cabinas
while not (cola_vacia(cabina1) and cola_vacia(cabina2) and cola_vacia(cabina3)):
    if not cola_vacia(cabina1):
        vehiculo = en_frente(cabina1)
        tarifa = vehiculo['tarifa']
        atencion(cabina1)
    if not cola_vacia(cabina2):
        vehiculo = en_frente(cabina2)
        tarifa = vehiculo['tarifa']
        atencion(cabina2)
    if not cola_vacia(cabina3):
        vehiculo = en_frente(cabina3)
        tarifa = vehiculo['tarifa']
        atencion(cabina3)

# Determinar qué cabina
# Realizar la atención de las cabinas
while not (cola_vacia(cabina1) and cola_vacia(cabina2) and cola_vacia(cabina3)):
    if not cola_vacia(cabina1):
        vehiculo = en_frente(cabina1)
        tarifa = vehiculo['tarifa']
        total[tipos_vehiculos.index(vehiculo['tipo'])] += tarifa # Sumar el valor de la tarifa al total de ingresos
    atencion(cabina1)
if not cola_vacia(cabina2):
    vehiculo = en_frente(cabina2)
    tarifa = vehiculo['tarifa']
    total[tipos_vehiculos.index(vehiculo['tipo'])] += tarifa # Sumar el valor de la tarifa al total de ingresos
    atencion(cabina2)
if not cola_vacia(cabina3):
    vehiculo = en_frente(cabina3)
    tarifa = vehiculo['tarifa']
    total[tipos_vehiculos.index(vehiculo['tipo'])] += tarifa # Sumar el valor de la tarifa al total de ingresos
    atencion(cabina3)

# Determinar qué cabina recaudó mayor cantidad de pesos
recaudacion_cabina1 = total[0] * listaContador[0]
recaudacion_cabina2 = total[1] * listaContador[1]
recaudacion_cabina3 = total[2] * listaContador[2]

if recaudacion_cabina1 > recaudacion_cabina2 and recaudacion_cabina1 > recaudacion_cabina3:
    print("La cabina 1 recaudó la mayor cantidad de pesos")
elif recaudacion_cabina2 > recaudacion_cabina1 and recaudacion_cabina2 > recaudacion_cabina3:
    print("La cabina 2 recaudó la mayor cantidad de pesos")
elif recaudacion_cabina3 > recaudacion_cabina1 and recaudacion_cabina3 > recaudacion_cabina2:
    print("La cabina 3 recaudó la mayor cantidad de pesos")
else:
    print("Las cabinas recaudaron la misma cantidad de pesos")

# Mostrar el número de vehículos de cada tipo que pasaron por las cabinas de peaje
print("Cantidad de vehículos de cada tipo que pasaron por las cabinas de peaje:")
for i in range(len(tipos_vehiculos)):
    print(f"{tipos_vehiculos[i]}: {listaContador[i]}")

# Mostrar el total de ingresos por tipo de vehículo
print("Total de ingresos por tipo de vehículo:")
for i in range(len(tipos_vehiculos)):
    print(f"{tipos_vehiculos[i]}: {total[i]}")
    
