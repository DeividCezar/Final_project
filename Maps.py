import Índice as i
import geopandas as gspd

# Importando layer do limite territorial para plotagem de mapas:

mapeamento = gspd.read_file('mapeamento.dbf')
mapeamento = gspd.read_file('mapeamento.shp')
mapeamento = gspd.read_file('mapeamento.shx')

# Funções para plotagem do mapa gráfico:

def plot_ind(m,y):
    '''
    m: mês;
    y: ano;
    Esta função retorna o mapa indicando o índice de criminalidade em cada município em uma determinada data (ano/mês).
    '''
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(i.indices_municipio.get_group(date).reset_index())
    complet_map = complet_map.plot(column='Índice', cmap='OrRd', legend=True, figsize=(18,9))
    return complet_map

## Regiões:

def plot_regioes():
    '''
    Esta função retorna o mapa indicando a separação entre as quatro regiões do estado do Rio de Janeiro: Interior, Baixada Fluminense, Grande Niterói e Rio de Janeiro.
    '''
    complet_map = mapeamento.join(i.indices_municipio.get_group('2014/01'))
    complet_map = complet_map.plot(column='Região', cmap='Paired', legend=True, figsize=(18,9))
    return complet_map

## Taxas agregadas:

def plot_taxa_agreg(m,y,var):
    '''
    m: mês ('dois dígitos');
    y: ano - ['2014', '2015', '2016', '2017', '2018'];
    var: índice agregado - ['Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']
    Esta função retorna o mapa indicando o índice agregado indicado em cada município em uma determinada data (ano/mês).
    '''
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(i.indices_agregados_mun.get_group(date)[var].reset_index())
    return(complet_map.plot(column=var, cmap='OrRd', legend=True, figsize=(18,9)))