import ee


def conecta_gee(proyecto):
    try:
        ee.Initialize(project=proyecto)
    except Exception as e:
        print(f"Error al conectar con GEE: {e}")
        print("Iniciando proceso de autenticación...")
        ee.Authenticate()
        ee.Initialize(project=proyecto)
