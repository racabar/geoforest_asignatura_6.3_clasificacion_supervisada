# Ejercicio 6.3. Clasificación supervisada

El alumno debe realizar su propia clasificación de especies o de usos de suelo de su municipio. Para ello debe:
- Elegir la imagen de entrada
- Calcular los índices que considere necesarios
- Introducir las bandas que considere necesarias
- Realizar una primera clasificación con Random Forest
- Analizar la importancia
- Realizar una segunda clasificación sólo con las variables más importantes
- Analizar los resultados obtenidos parciales y finales

En este ejercicio he optado por utilizar un notebook porque es más visual para crear gráficos y mapas que un script de Python e incluso la interfaz de la consola de GEE.

Los polígonos de etiquetado están en el geopackage entradas/infoVectorial.gpkg.

## Resultado primera clasificación

Tras hacer una primera clasificación, usando toda la información de las bandas de Sentinel-2, Sentinel-1 y los índices NDVI, NDTI, MNDWI, he obtenido la siguiente matriz de validación.

```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 22, 2, 4, 3],
 [0, 0, 1, 12, 0, 0],
 [0, 1, 1, 1, 14, 0],
 [0, 0, 1, 0, 5, 4]]
```
Esta configuración ha devuelto un valor de precisión de la validación de 0.7397260273972602.

He intentado añadir algún índice de suelo como el BSI, pero bajaba bastante la puntuación y la clasificación, por lo que lo he desechado.

El código de esta clasificación está en el notebook 03.1_supervisada.ipynb y el resultado en 03.1_supervisada.html.

Los mapas están en la carpeta salidas/mapas_html_supervisada, donde se puede consultar también la clasificación.

## Resultado tras ajuste de bandas

Una vez hecha la primera clasificación he estado configurando las bandas utilizadas para hacer ésta para intentar mejorarla, pero no he conseguido nada mejor. A continuación muestro parte de las pruebas que he estado haciendo.

El código de esta clasificación está en el notebook 03.1_supervisada_ajustada.ipynb y el resultado en 03.1_supervisada_ajustada.html. Los mapas están en la carpeta salidas/mapas_html_supervisada_ajustada, donde se puede consultar también la clasificación.

A pesar de que hay varias pruebas con una puntuación de validación de 0,69, creo que la que mejor se ajusta es la primera de las de a continuación porque, aunque la puntuación sea menor, la dispersión de los datos también lo es, repartiendo menos los errores, de manera que solo hay errores en una clase o como mucho dos, mientras que en el resto de clasificaciones los errores se reparten más.   

**B2, VH, MNDWI, NDTI**
```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 22, 3, 0, 6],
 [0, 0, 2, 11, 0, 0],
 [0, 5, 0, 0, 12, 0],
 [0, 0, 1, 0, 6, 3]]
Precisión de la validación: 0.684931506849315
```

**B11, B12, NDVI, MNDWI**
```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 24, 1, 3, 3],
 [0, 0, 4, 8, 0, 1],
 [0, 3, 2, 1, 11, 0],
 [0, 0, 0, 3, 1, 6]]
Precisión de la validación: 0.6986301369863014
```

**B11, B12, B5, NDVI**
```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 19, 11, 0, 1],
 [0, 0, 1, 8, 0, 4],
 [0, 0, 1, 3, 13, 0],
 [0, 0, 0, 1, 0, 9]]
Precisión de la validación: 0.6986301369863014
```

**B11, B12, NDVI**
```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 25, 1, 3, 2],
 [0, 0, 5, 7, 0, 1],
 [0, 3, 0, 3, 5, 6],
 [0, 0, 0, 1, 3, 6]]
Precisión de la validación: 0.6164383561643836
```

**B11, B12, MNDWI**
```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 0],
 [0, 0, 24, 3, 2, 2],
 [0, 0, 1, 11, 0, 1],
 [0, 4, 0, 3, 5, 5],
 [0, 0, 0, 4, 0, 6]]
Precisión de la validación: 0.6301369863013698
```

**B12, B5, NDVI**
```
Matriz de validación:
[[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 21, 4, 1, 5],
 [0, 0, 2, 8, 0, 3],
 [0, 0, 1, 0, 8, 8],
 [0, 0, 1, 2, 3, 4]]
Precisión de la validación: 0.589041095890411
```