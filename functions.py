import requests
from bs4 import BeautifulSoup

import os
import json 
import pandas as pd

# -----------------------------------------------------------------------------
def init():
    global dir_root, dir_data, dir_tmp, dir_report, dir_download
    dir_root = os.path.abspath(os.getcwd())
    createStructure()

def createStructure():
    globals()["dir_data"] = globals()["dir_root"]+'/data/'
    os.makedirs(globals()["dir_data"], exist_ok = True)

    globals()["dir_tmp"] = globals()["dir_root"]+'/tmp/'
    globals()["dir_download"] = globals()["dir_tmp"]+'/download/'
    os.makedirs(globals()["dir_download"], exist_ok = True)

    globals()["dir_report"] = globals()["dir_root"]+'/report/'
    os.makedirs(globals()["dir_report"], exist_ok = True)

# -----------------------------------------------------------------------------
def file_put_contents(filename, content,mode="w"):
    with open(filename, mode) as f_in: 
        f_in.write(content)

def file_get_contents(filename, mode="r"):
    with open(filename, mode) as f_in: 
        return f_in.read()      

# -----------------------------------------------------------------------------
def exportToCsv(data, file_path):
    ds = pd.DataFrame(data)
    ds.to_csv(file_path, index = False, header = None)

def download(url):
    file_name = os.path.basename(url)
    file_path = globals()["dir_download"]+file_name
    if not os.path.isfile(file_path) :
        r = requests.get(url)  
        file_put_contents(file_path, r.content, "wb")
    return file_path

# -----------------------------------------------------------------------------
def getEstaciones(file_path):
    html = file_get_contents(file_path)

    # Scrappig
    soup = BeautifulSoup(html, "html.parser")
    
    # Buscamos todos los elementos html del tipo LI con attributo data-gmapping
    elements = soup.findAll("li", {"data-gmapping" : True})

    estaciones = [['id','name','lat','lon','type']]
    for ele in elements :
        # convertimos el atributo data-gmapping a formato json
        data_gmapping = json.loads(ele["data-gmapping"])

        # convertimos el json en lista
        estaciones.append([
            data_gmapping['id'],
            data_gmapping['text'],
            data_gmapping['latlng']['lat'],
            data_gmapping['latlng']['lng'],
            data_gmapping['tipo']
        ])       

    return estaciones
