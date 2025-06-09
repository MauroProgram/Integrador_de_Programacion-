import random
import time
import tracemalloc  # Mide consumo de memoria

# Paso 1: Crear una lista base con 15 jugadores reales
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

# Paso 2: Expandir con 9.985 jugadores ficticios con goles aleatorios
for i in range(9985):
    jugadores_goles.append({
        'nombre': f'Jugador Ficticio {i+1}',
        'goles_champions': random.randint(1, 80)
    })

# Paso 3: Mezclar aleatoriamente la lista
random.shuffle(jugadores_goles)

# Paso 4: Implementación de Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[0]
    menores = [x for x in arr[1:] if x['goles_champions'] <= pivote['goles_champions']]
    mayores = [x for x in arr[1:] if x['goles_champions'] > pivote['goles_champions']]
    return quick_sort(mayores) + [pivote] + quick_sort(menores)

# Paso 5: Medir tiempo y memoria
tracemalloc.start()
inicio = time.time()

jugadores_ordenados = quick_sort(jugadores_goles)

fin = time.time()
mem_actual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Paso 6: Mostrar resultados
print("\n--- Resultados del Ordenamiento (Quick Sort) con 10.000 jugadores ---")
print(f"Tiempo de ejecución: {fin - inicio:.8f} segundos")
print(f"Uso actual de memoria: {mem_actual / 1024:.2f} KB")
print(f"Pico máximo de memoria: {mem_pico / 1024:.2f} KB")
print(f"Máximo goleador tras ordenamiento: {jugadores_ordenados[0]['nombre']} con {jugadores_ordenados[0]['goles_champions']} goles")
