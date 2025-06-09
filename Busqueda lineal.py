import time
import random
jugadores_goles = [
    {'nombre': 'Cristiano Ronaldo', 'goles_champions': 140},
    {'nombre': 'Lionel Messi', 'goles_champions': 129},
    {'nombre': 'Robert Lewandowski', 'goles_champions': 94},
    {'nombre': 'Karim Benzema', 'goles_champions': 90},
    {'nombre': 'Raúl González', 'goles_champions': 71},
    {'nombre': 'Thomas Müller', 'goles_champions': 54},
    {'nombre': 'Thierry Henry', 'goles_champions': 50},
    {'nombre': 'Kylian Mbappé', 'goles_champions': 48},
    {'nombre': 'Zlatan Ibrahimović', 'goles_champions': 48},
    {'nombre': 'Mohamed Salah', 'goles_champions': 44},
    {'nombre': 'Neymar Jr.', 'goles_champions': 43},
    {'nombre': 'Erling Haaland', 'goles_champions': 41},
    {'nombre': 'Ángel Di María', 'goles_champions': 41},
    {'nombre': 'Filippo Inzaghi', 'goles_champions': 41},
    {'nombre': 'Andriy Shevchenko', 'goles_champions': 41}
]
# Añadir 85 jugadores ficticios con valores aleatorios de goles
for i in range(85):
    jugadores_goles.append({
        'nombre': f'Jugador Ficticio {i+1}',
        'goles_champions': random.randint(1, 80)
    })

# Desordenar la lista completa
random.shuffle(jugadores_goles)

# Mostrar una muestra aleatoria de 5 jugadores
print("--- Muestra de la Lista Desordenada ---")
for jugador in jugadores_goles[:5]:
    print(f"{jugador['nombre']}: {jugador['goles_champions']} goles")

def busqueda_lineal(lista_jugadores):
    """
    Recorre la lista completa y retorna al jugador con más goles en Champions League.
    Complejidad temporal: O(n)
    """
    if not lista_jugadores:
        return None  # Caso borde: lista vacía

    max_goleador = lista_jugadores[0]  # Suponemos inicialmente que es el primero
    for jugador in lista_jugadores[1:]:
        if jugador['goles_champions'] > max_goleador['goles_champions']:
            max_goleador = jugador  # Se actualiza si se encuentra un valor mayor
    return max_goleador

# Medición del tiempo de ejecución
tiempo_inicio = time.time()
goleador_maximo = busqueda_lineal(jugadores_goles)
tiempo_fin = time.time()
tiempo_busqueda_lineal = tiempo_fin - tiempo_inicio

# Resultados
print(f"Máximo Goleador (Búsqueda Lineal): {goleador_maximo['nombre']} con {goleador_maximo['goles_champions']} goles")
print(f"Tiempo de ejecución: {tiempo_busqueda_lineal:.8f} segundos")
