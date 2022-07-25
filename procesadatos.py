#! /usr/bin/env python3

# Script para procesar los datos de la AEMET 

import matplotlib.pyplot as plt
import pandas as pd

TInfernal = 35
THorror = 37
TMuerte = 39

añoInicial = 2000
añoFinal = 2022

# código de las estaciones
# Madrid-Retiro: 3195
# Ávila: 2444
# Ponferrada: 1549

estacion = "3195"
nombreEstacion = "Madrid"

# preparar un data frame de resultados al que iremos añadiendo los datos de cada año
# filas los años, columnas año/tmax35/tmax37/tmax39
columnas = ['Año','tmax35', 'tmax37', 'tmax39']
dfResumen = pd.DataFrame(columns=columnas)

for añoEnCurso in range(añoInicial, añoFinal + 1):
    filename = "datos" + str(añoEnCurso) + nombreEstacion + ".json"
    print ("Procesando datos del fichero: " + filename)
    da = pd.read_json(filename)
    dfloat = da.tmax.str.replace(',', '.').astype(float)
    dfResumen.loc[len(dfResumen)] = [añoEnCurso, (dfloat[dfloat >= TInfernal]).count(), (dfloat[dfloat >= THorror]).count(),
            (dfloat[dfloat >= TMuerte]).count()]
print(dfResumen)

# representación en un gráfico de barras
plt.rcParams["figure.figsize"] = (15, 10)
dfResumen.plot.bar(x="Año", color=['pink', 'orange', 'red'], rot=30, 
  title="Días en que la temperatura máxima superó 3 umbrales. Observatorio de " + nombreEstacion);
plt.show(block=True);