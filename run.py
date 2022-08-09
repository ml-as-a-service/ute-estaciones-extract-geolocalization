import functions as fx
# -----------------------------------------------------------------------------
# Inicializamos la estructura de carpetas
fx.init()

# -----------------------------------------------------------------------------
# Bajamos la pagina en tmp/download/MapaEstHid.aspx utilizando requests
url = "https://apps.ute.com.uy/SgePublico/MapaEstHid.aspx"
file_path = fx.download(url)

# -----------------------------------------------------------------------------
# Obtenemos las estaciones en una lista utilizando BeautifulSoup
estaciones = fx.get_estaciones(file_path)

# -----------------------------------------------------------------------------
# Exportamos las estaciones a CSV utilizando pandas
file_name_csv = "MapaEstHid.csv"
file_path_csv = fx.dir_data+file_name_csv
fx.export_to_csv(estaciones, file_path_csv)
