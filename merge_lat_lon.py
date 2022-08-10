import functions as fx

import pandas as pd 
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# -----------------------------------------------------------------------------
# Aproximacion por Distancia Levenshtein
# -----------------------------------------------------------------------------


# id                    name        lat        lon      type
df_MapaEstHid = pd.read_csv('./data/MapaEstHid.csv')
#cuenca          subcuenca               x1       estacion  nivel  x2  x3                   dt
df_ute = pd.read_csv('./data/2000-Enero-2000-Junio-BAYGO-SDBAYGO-UBAYGO-PTOROS.csv')


df_ute_name = df_ute['estacion'].unique()
df_MapaEstHid_name = df_MapaEstHid['name'].unique()

# print(df_ute_name, df_MapaEstHid_name)

df_ute_sinonimos = []
for e in df_MapaEstHid_name:
  near = process.extractOne(e, df_ute_name)
  df_ute_sinonimos.append([e,near[0],near[1]])
df_ute_sinonimos = pd.DataFrame(df_ute_sinonimos, columns=['estacion_raw', 'name','distance'])

df_ute_sinonimos = df_ute_sinonimos.sort_values('distance',ascending=False)
print(df_ute_sinonimos)

df_ute_sinonimos = df_ute_sinonimos.query(" distance == distance.max() ")

# Merge

df_ute_sinonimos = pd.merge( df_ute_sinonimos, 
                                    df_MapaEstHid[['name','lat','lon']], 
                                    left_on="name", right_on="name", 
                                    how="left", 
                                    sort=False)
print(df_ute_sinonimos)


# # -----------------------------------------------------------------------------
# # Aproximacion por Distancia Levenshtein
# # -----------------------------------------------------------------------------

# id                    name        lat        lon      type
df_MapaEstHid = pd.read_csv('./data/MapaEstHid.csv')
#cuenca          subcuenca               x1       estacion  nivel  x2  x3                   dt
df_ute = pd.read_csv('./data/2000-Enero-2000-Junio-BAYGO-SSALSI-SARBOL-SALSI.csv')


df_ute_name = df_ute['estacion'].unique()
df_MapaEstHid_name = df_MapaEstHid['name'].unique()

# print(df_ute_name, df_MapaEstHid_name)

df_ute_sinonimos = []
for e in df_MapaEstHid_name:
  near = process.extractOne(e, df_ute_name)
  df_ute_sinonimos.append([e,near[0],near[1]])
df_ute_sinonimos = pd.DataFrame(df_ute_sinonimos, columns=['estacion_raw', 'name','distance'])

df_ute_sinonimos = df_ute_sinonimos.sort_values('distance',ascending=False)
print(df_ute_sinonimos)

df_ute_sinonimos = df_ute_sinonimos.query(" distance == distance.max() ")

# Merge

df_ute_sinonimos = pd.merge( df_ute_sinonimos, 
                                    df_MapaEstHid[['name','lat','lon']], 
                                    left_on="name", right_on="name", 
                                    how="left", 
                                    sort=False)
print(df_ute_sinonimos)

