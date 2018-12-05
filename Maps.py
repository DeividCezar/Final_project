import Índice as i
import geopandas as gspd

# Importando layer do limite territorial para plotagem de mapas:

mapeamento = gspd.read_file('mapeamento.dbf')
mapeamento = gspd.read_file('mapeamento.shp')
mapeamento = gspd.read_file('mapeamento.shx')

# Funções para plotagem do mapa gráfico:

def plot_ind(m,y):
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(i.indices_municipio.get_group(date).reset_index())
    complet_map = complet_map.plot(column='Índice', cmap='OrRd', legend=True, figsize=(18,9))
    return complet_map

## Regiões:

def plot_regioes():
    complet_map = mapeamento.join(i.indices_municipio.get_group('2014/01'))
    complet_map = complet_map.plot(column='Região', cmap='Paired', legend=True, figsize=(18,9))
    return complet_map

## Taxas agregadas:

def plot_taxa_agreg(m,y,var):
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(i.indices_agregados_mun.get_group(date)[var].reset_index())
    return(complet_map.plot(column=var, cmap='OrRd', legend=True, figsize=(18,9)))