import requests

def obtener_datos(endpoint, parametro=""):
    url = f"https://pokeapi.co/api/v2/{endpoint}/{parametro}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        print("Error al hacer la petición:", respuesta.status_code)
        return None

datos = obtener_datos("pokemon", "25")  # Pikachu

if datos:
    print(f"Nombre: {datos['name'].title()}")
    print(f"Altura: {datos['height']}")
    print(f"Peso: {datos['weight']}")
