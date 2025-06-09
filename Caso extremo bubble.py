import random
import time
import tracemalloc  # Para medir el uso de memoria

# Crear una lista base de 15 jugadores reales
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

# Agregar 9.985 jugadores ficticios
for i in range(9985):
    jugadores_goles.append({
        'nombre': f'Jugador Ficticio {i+1}',
        'goles_champions': random.randint(1, 80)
    })

# Mezclar la lista aleatoriamente
random.shuffle(jugadores_goles)

# Bubble Sort (versión descendente)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['goles_champions'] < arr[j + 1]['goles_champions']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Medición de tiempo y memoria
tracemalloc.start()
inicio = time.time()

jugadores_ordenados = bubble_sort(jugadores_goles)

fin = time.time()
mem_actual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Resultados
print("\n--- Resultados del Ordenamiento (Bubble Sort) con 10.000 jugadores ---")
print(f"Tiempo de ejecución: {fin - inicio:.8f} segundos")
print(f"Uso actual de memoria: {mem_actual / 1024:.2f} KB")
print(f"Pico máximo de memoria: {mem_pico / 1024:.2f} KB")
print(f"Máximo goleador tras ordenamiento: {jugadores_ordenados[0]['nombre']} con {jugadores_ordenados[0]['goles_champions']} goles")
