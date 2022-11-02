#! /usr/bin/env python3

# Script para objeter los datos de la AEMET 

import requests
import json
import os.path

# Variables de entrada y preparacion de la petición

apiKey = "usar la otorgada por AEMET"

añoInicial = 2000
añoFinal = 2022

# código de las estaciones
# Madrid-Retiro: 3195
# Ávila: 2444
# Ponferrada: 1549

estacion = "3195"
nombreEstacion = "Madrid"

# bucle principal, baja datos y crea un fichero por año
for añoEnCurso in range(añoInicial, añoFinal+1):
  # verificar que el fichero no está ya bajado, para no castigar demasiado a AEMET
  filename = "datos" + str(añoEnCurso) + nombreEstacion + ".json"
  print("Datos para el año: " + str(añoEnCurso))
  if (os.path.isfile(filename)):
    print("Fichero para el año: " + str(añoEnCurso) + " ya estaba bajado")
  else:    
    urlPeticion = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/" + str(añoEnCurso) + "-04-01T00%3A00%3A00UTC/fechafin/" + str(añoEnCurso) + "-10-31T00%3A00%3A00UTC/estacion/" + estacion
    print(urlPeticion)

    querystring = {"api_key": apiKey}
    headers = {
        'cache-control': "no-cache"
        }
    response = requests.request("GET", urlPeticion, headers=headers, params=querystring)
    print(response.text)

    # del resultado JSON sólo nos interesa el campo "datos" que contiene una URL
    urlDatos = response.json().get("datos")
    print("URL con los datos: ", urlDatos)
    response = requests.request("GET", urlDatos, headers=headers)

    # almacenar datos en un fichero
    # filename = "datos" + str(añoEnCurso) + nombreEstacion + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
        f.close()
  # end if(file does not exist)
# fin del bucle
print("¡Se acabó!")

