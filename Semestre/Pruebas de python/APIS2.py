import requests

# URL de ejemplo para consultar el PIB de México desde la World Bank API
url = "https://api.worldbank.org/v2/country/mx/indicator/NY.GDP.MKTP.CD?format=json"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print(datos)
else:
    print("Error al conectar con la API:", respuesta.status_code)
print(url)
