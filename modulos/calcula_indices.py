# https://github.com/awesome-spectral-indices/spyndex/

import spyndex


def calcula_indices_spyndex(imagen_con_bandas_espectrales, lista_indices):
    # Mapeo las bandas de Sentinel-2 a parámetros de spyndex
    # https://github.com/awesome-spectral-indices/spyndex
    params = {
        "B": imagen_con_bandas_espectrales.select("B2"),
        "G": imagen_con_bandas_espectrales.select("B3"),
        "R": imagen_con_bandas_espectrales.select("B4"),
        "RE1": imagen_con_bandas_espectrales.select("B5"),
        "RE2": imagen_con_bandas_espectrales.select("B6"),
        "RE3": imagen_con_bandas_espectrales.select("B7"),
        "N": imagen_con_bandas_espectrales.select("B8"),
        "N2": imagen_con_bandas_espectrales.select("B8A"),
        "S1": imagen_con_bandas_espectrales.select("B11"),
        "S2": imagen_con_bandas_espectrales.select("B12")
    }

    # Calculo los índices
    # Si se pasa una lista de índices, devuelve una imagen multibanda
    indices = spyndex.computeIndex(
        index=lista_indices,
        params=params
    )

    return indices
