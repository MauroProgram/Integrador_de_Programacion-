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


def quick_sort(lista):
    """
    Ordena recursivamente una lista de jugadores en orden descendente por goles usando Quick Sort.
    Complejidad promedio: O(n log n)
    """
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        mayores = [jugador for jugador in lista[1:] if jugador['goles_champions'] >= pivote['goles_champions']]
        menores = [jugador for jugador in lista[1:] if jugador['goles_champions'] < pivote['goles_champions']]
        return quick_sort(mayores) + [pivote] + quick_sort(menores)

# Medición de tiempo
jugadores_copia = copy.deepcopy(jugadores_goles)  # Evitar alterar la lista original

tiempo_inicio = time.time()
lista_ordenada_quick = quick_sort(jugadores_copia)
tiempo_fin = time.time()
tiempo_quick_sort = tiempo_fin - tiempo_inicio

# Resultados
print(f"Máximo Goleador (Quick Sort): {lista_ordenada_quick[0]['nombre']} con {lista_ordenada_quick[0]['goles_champions']} goles")
print(f"Tiempo de ejecución: {tiempo_quick_sort:.8f} segundos")
