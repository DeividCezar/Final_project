# Importando módulo Índice e bibliotecas necessárias:

import Índice as i
import pandas as pd
import numpy as np
import altair as alt
import geopandas as gspd


# Importando layer do limite territorial para plotagem de mapas:

mapeamento = gspd.read_file('mapeamento.dbf')
mapeamento = gspd.read_file('mapeamento.shp')
mapeamento = gspd.read_file('mapeamento.shx')



#### REGIÃO DOS LAGOS:

# Índices agregados da Região dos Lagos:

smt_rl_grupos = i.smt_mun_grupos[(i.smt_mun_grupos.Município == 'Araruama') | (i.smt_mun_grupos.Município == 'Saquarema') | (i.smt_mun_grupos.Município == 'Arraial do Cabo') | (i.smt_mun_grupos.Município == 'Armação dos Búzios') | (i.smt_mun_grupos.Município == 'São Pedro da Aldeia') | (i.smt_mun_grupos.Município == 'Iguaba Grande') | (i.smt_mun_grupos.Município == 'Cabo Frio')]
indices_agregados_rl = smt_rl_grupos.groupby('Data').mean()
indices_agregados_rl = indices_agregados_rl.reset_index()
separate_data = indices_agregados_rl['Data'].str.split('/', expand=True)
separate_data.columns=['Ano', 'Mês']
indices_agregados_rl = indices_agregados_rl.join(separate_data['Ano'])
indices_agregados_rl = indices_agregados_rl.join(separate_data['Mês'])

# Índice de criminalidade na Região dos Lagos:

indice_rl = i.indices_mun[(i.indices_mun.Município == 'Araruama') | (i.indices_mun.Município == 'Saquarema') | (i.indices_mun.Município == 'Arraial do Cabo') | (i.indices_mun.Município == 'Armação dos Búzios') | (i.indices_mun.Município == 'São Pedro da Aldeia') | (i.indices_mun.Município == 'Iguaba Grande') | (i.indices_mun.Município == 'Cabo Frio')]
indice_rl = indice_rl.groupby('Data').mean()
indice_rl = indice_rl.reset_index()
i_separate_data_rl = indice_rl['Data'].str.split('/', expand=True)
i_separate_data_rl.columns=['Ano', 'Mês']
indice_rl = indice_rl.join(i_separate_data_rl['Ano'])
indice_rl = indice_rl.join(i_separate_data_rl['Mês'])

# Plotagem do índice para Região dos Lagos:

plot_ind_rl = alt.Chart(indice_rl).mark_line().encode(
    x = 'Mês',
    y = 'Índice',
    color = 'Ano:N'
).properties(
    width = 800,
    height = 300,
        title = 'Índice de criminalidade na Região dos Lagos'
)
    
# Criando coluna para verificação dos municípios da Região dos Lagos (plotagem da região destacada):

map_r = np.array(mapeamento['nome'])
rl = []

for j in list(map_r):
    if j in ['Araruama', 'Saquarema', 'Arraial do Cabo', 'Armação dos Búzios', 'São Pedro da Aldeia', 'Iguaba Grande', 'Cabo Frio']:
        t = 'Região dos Lagos'
    else:
        t = 'Restante do estado'
    rl.append(t)

v_rl = pd.DataFrame(rl)
v_rl.columns = ['Pertence a Região dos Lagos'] 

mapa_rl_destacada = mapeamento.join(v_rl)

    
#### REGIÃO METROPOLITANA:    

# Índices agregados na Região Metropolitana:

smt_rm_grupos = i.smt_mun_grupos[i.smt_mun_grupos['Região'] != 'Interior']
indices_agregados_rm = smt_rm_grupos.groupby('Data').mean()
indices_agregados_rm = indices_agregados_rm.reset_index()
separate_data_rm = indices_agregados_rm['Data'].str.split('/', expand=True)
separate_data_rm.columns=['Ano', 'Mês']
indices_agregados_rm = indices_agregados_rm.join(separate_data_rm['Ano'])
indices_agregados_rm = indices_agregados_rm.join(separate_data_rm['Mês'])

# Criando coluna para verificação da Região Metropolitana (plotagem da região destacada):

map_rm = np.array(i.indices_municipio.get_group('2014/01')['Região'])
rm = []

for j in list(map_rm):
    if j in ['Baixada Fluminense', 'Rio de Janeiro', 'Grande Niterói']:
        t = "Região Metropolitana"
    else:
        t = "Restante do estado"
    rm.append(t)

v_rm = pd.DataFrame(rm)
v_rm.columns = ['Pertence a Região Metropolitana'] 

mapa_rm_destacada = mapeamento.join(v_rm)

    
#### CAPITAL (Rio de Janeiro):
    
# Índices agregados no município do Rio de Janeiro:
    
smt_rj_grupos = i.smt_mun_grupos[i.smt_mun_grupos['Município'] == 'Rio de Janeiro']
indice_rj = smt_rj_grupos.reset_index()
separate_data_rj = indice_rj['Data'].str.split('/', expand=True)
separate_data_rj.columns=['Ano', 'Mês']
indice_rj = indice_rj.join(separate_data_rj['Ano'])
indice_rj = indice_rj.join(separate_data_rj['Mês'])
    
# Criando coluna para verificação do Município do Rio de Janeiro (plotagem da região destacada):

rj = []

for j in list(map_r):
    if j == 'Rio de Janeiro':
        t = 'Rio de Janeiro'
    else:
        t = 'Restante do estado'
    rj.append(t)

v_rj = pd.DataFrame(rj)
v_rj.columns = ['Rio de Janeiro'] 

mapa_rj_destacado = mapeamento.join(v_rj)

    
# Função para plotagem dos índices agregados:

def plot_chart(data_frame, variável):
    chart = alt.Chart(data_frame).mark_line().encode(
        x = 'Mês',
        y = variável,
        color = 'Ano:N'
    ).properties(
        width = 800,
        height = 300,
        title = 'Taxas criminais - '+variável+' (a cada cem mil habitantes)'
    )
    return(chart)

    
# Funções para plotagem do mapa gráfico:

def plot_map(m,y):
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(indices_agregados_mun.get_group(date)['Furtos'].reset_index())
    return(complet_map.plot(column='Furtos', cmap='OrRd', legend=True, figsize=(12,5)))