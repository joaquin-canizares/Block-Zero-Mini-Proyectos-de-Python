import requests

ciudad = input("De que ciudad quieres saber el clima: ")

url = "https://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid=bbbc2b69c7ab6453d8b2ebd1a3e248db&units=metric&lang=es"
respuesta = requests.get(url)
datos = respuesta.json()
try:

    print("Ciudad:", datos["name"])
    print("Temperatura:", datos["main"]["temp"])
    print("Descripcion:", datos["weather"][0]["description"])
except:
    print("Ciudad no encontrada")