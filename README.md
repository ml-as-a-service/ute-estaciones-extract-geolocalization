# Consulta Geográfica de Estaciones Hidrometeorológicas.

Desde la pagina [https://apps.ute.com.uy/SgePublico/MapaEstHid.aspx](https://apps.ute.com.uy/SgePublico/MapaEstHid.aspx) 
extaemos la información de las Estaciones Hidrometeorológicas. 
Para lo cual utilizaremos los paquetes:
 - **Request**: permitirá realizar peticiones HTTP, FTP, etc
 - **BeautifulSoup**:  librería Python que permite extraer información de contenido en formato HTML o XML 
 - **Pandas**: es una librería de Python especializada en el manejo y análisis de estructuras de datos

## Instalacion de dependencias
Instalamos las librerias dependientes desde requirements.txt

```bash
pip3 install -r requirements.txt
```

## Ejecutar
Al ejecutar el comando 

```bash
python run.py
```
Se procedera a:
 - crear la estructura de directorios
 - descargar el archivo fuente en la carpeta tmp/download
 - exportar la informacion de las estaciones que se encuentran en el archivo a csv, el mismo se guardara en la carpeta data/


