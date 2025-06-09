import random
import time
import copy
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





def insertion_sort(lista_jugadores):
    """
    Ordena la lista de jugadores en orden descendente por goles usando Insertion Sort.
    Complejidad temporal: O(n²) en el peor caso.
    """
    for i in range(1, len(lista_jugadores)):
        actual = lista_jugadores[i]
        j = i - 1
        # Desplazamos elementos mayores hasta encontrar la posición correcta
        while j >= 0 and lista_jugadores[j]['goles_champions'] < actual['goles_champions']:
            lista_jugadores[j + 1] = lista_jugadores[j]
            j -= 1
        lista_jugadores[j + 1] = actual
    return lista_jugadores

# Medición de tiempo para ordenar y extraer al máximo goleador
jugadores_copia = copy.deepcopy(jugadores_goles)  # Copia para no alterar el original

tiempo_inicio = time.time()
lista_ordenada_insertion = insertion_sort(jugadores_copia)
tiempo_fin = time.time()
tiempo_insertion_sort = tiempo_fin - tiempo_inicio

# Resultados
print(f"Máximo Goleador (Insertion Sort): {lista_ordenada_insertion[0]['nombre']} con {lista_ordenada_insertion[0]['goles_champions']} goles")
print(f"Tiempo de ejecución: {tiempo_insertion_sort:.8f} segundos")
