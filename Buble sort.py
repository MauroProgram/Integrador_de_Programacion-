
import random
import time
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
def bubble_sort(lista_jugadores):
    """
    Ordena la lista de jugadores por goles en orden descendente usando Bubble Sort.
    Complejidad temporal: O(n²)
    """
    n = len(lista_jugadores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_jugadores[j]['goles_champions'] < lista_jugadores[j + 1]['goles_champions']:
                # Intercambio de elementos si están en orden incorrecto
                lista_jugadores[j], lista_jugadores[j + 1] = lista_jugadores[j + 1], lista_jugadores[j]
    return lista_jugadores

# Medición de tiempo para ordenar y obtener al máximo goleador
import copy
jugadores_copia = copy.deepcopy(jugadores_goles)  # Evitamos modificar el original

tiempo_inicio = time.time()
lista_ordenada_bubble = bubble_sort(jugadores_copia)
tiempo_fin = time.time()
tiempo_bubble_sort = tiempo_fin - tiempo_inicio

# Resultados
print(f"Máximo Goleador (Bubble Sort): {lista_ordenada_bubble[0]['nombre']} con {lista_ordenada_bubble[0]['goles_champions']} goles")
print(f"Tiempo de ejecución: {tiempo_bubble_sort:.8f} segundos")
