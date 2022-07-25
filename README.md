# meteo

Scripts para jugar con los datos de AEMET y comprobar cómo se va degradando nuestra calidad de vida según aumenta el número de días de verano en que no se puede salir de casa.

Dos scripts:
- el primero, *bajadatos.py*, hace unas queries al portal de datos abiertos de AEMET https://opendata.aemet.es/centrodedescargas/inicio y almacena los datos en una serie de ficheros JSON, uno por año. Para usarlo es necesario hacerse con una API Key en el mismo portal.
- el segundo, *procesadatos.py* cuenta el número de días que se supera cierto umbral de temperatura máxima (35ºC, 37ºC, 30ºC) en cada año y lo representa en un gráfico de barras.

Se pueden consultar los datos de cualquier estación meteorológica; para ver su código, recomiendo hacer una consulta sencilla usando el "acceso general" (queries no programáticas) en https://opendata.aemet.es/centrodedescargas/productosAEMET.


