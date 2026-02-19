import ee

# Inicialización (asegúrate de haber hecho ee.Authenticate() previamente si es la primera vez)
try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

# 1. Configuración
roi = ee.Geometry.Point([-3.57987108, 37.11747003])
fecha_inicio = '2025-04-01'
fecha_fin = '2025-04-30'

# 2. Sentinel-2 (Óptico)
# Seleccionamos la imagen con menor porcentaje de nubes
s2_img = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
          .filterBounds(roi)
          .filterDate(fecha_inicio, fecha_fin)
          .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
          .sort('CLOUDY_PIXEL_PERCENTAGE')
          .first())

# 3. Sentinel-1 (Radar)
# Seleccionamos la primera imagen en modo IW, Descendente y Polarización VV
s1_img = (ee.ImageCollection('COPERNICUS/S1_GRD')
          .filterBounds(roi)
          .filterDate(fecha_inicio, fecha_fin)
          .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
          .filter(ee.Filter.eq('instrumentMode', 'IW'))
          .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
          .first())

# 4. Procesamiento y Extracción de Datos (Client-side)
print("Consultando metadatos en el servidor de Google...")

try:
    # Traemos los IDs y el porcentaje de nubes
    s2_id = s2_img.id().getInfo()
    s1_id = s1_img.id().getInfo()

    # Obtenemos el porcentaje de nubes (metadata del granulo)
    cloud_pct = s2_img.get('CLOUDY_PIXEL_PERCENTAGE').getInfo()

    # Cálculo de diferencia temporal
    t_s2 = s2_img.get('system:time_start')
    t_s1 = s1_img.get('system:time_start')

    diff_days = (ee.Number(t_s2).subtract(ee.Number(t_s1))
                 .abs()
                 .divide(1000 * 60 * 60 * 24)
                 .getInfo())

    # 5. Reporte en Consola
    print('\n--- REPORTE DE FUSIÓN (Python) ---')
    print(f'ID Sentinel-2 (Óptico): {s2_id}')
    print(f'Cobertura de Nubes:     {cloud_pct:.2f}%')
    print(f'ID Sentinel-1 (Radar):  {s1_id}')
    print(f'Diferencia Temporal:    {diff_days:.2f} días')

except Exception as e:
    print(f"\nError: {e}")