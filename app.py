import time

start_time = time.time()

# Función para filtrar URLs
def filtrar_urls(archivo):
    # Leer el archivo y filtrar URLs válidas
    urls_validas = {line.strip() for line in open(archivo) if line.strip() and "shop" in line and line.strip().endswith(".html")}

    # Mostrar resultados
    total_validas = len(urls_validas)
    print(f"Número total de URLs que cumplen con los criterios: {total_validas}")
    print("URLs válidas que cumplen con los criterios:")
    print("\n".join(urls_validas) if total_validas > 0 else "No se encontraron URLs válidas.")

# Llamar a la función con el nombre del archivo que contiene las URLs
filtrar_urls('urls.txt')

end_time = time.time()
print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos.")


