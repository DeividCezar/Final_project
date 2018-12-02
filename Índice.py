import pandas as pd
import numpy as np
import Dados as dd
import altair as alt
import geopandas as gspd

# Criação do índice de criminalidade e dos índices em grupo:

## Criação do índice de criminalidade:

### Importando as penas e criado a pena média:
penas_criminais = pd.read_excel("Dados_penas.xlsx")
penas_criminais['Pena média'] = (penas_criminais['Pena mínima'] + penas_criminais['Pena máxima'])/2

### Plotagem das penas:
plot_penas = alt.Chart(penas_criminais).mark_bar().encode(
    x='Crime',
    y='Pena média'
).configure_mark(
    opacity=0.8,
    color='red'
).properties(
  width=880,
  height=250
)

### Criação do índice de criminalidade para os municípios:

#### Excluindo colunas desnecessárias para o índice:
smt_crimes = dd.serie_municipal_taxas.drop(['Data', 'Região', 'Município', 'Ano', 'Mês', 'Homicídio por Intervenção Policial', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos',  'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências'], axis=1)

smt_crimes = np.array(smt_crimes)
smt_mun = pd.DataFrame(smt_crimes, dtype=float)

smt_mun.columns = ['Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Total de Roubos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Ameaças']

#### Criando índice de criminalidade:

array_average_mun = np.array(smt_mun)
indices_mun = np.average(array_average_mun, weights = penas_criminais['Pena média'], axis = 1)
indices_mun = pd.DataFrame(indices_mun)
indices_mun['Município'] = np.array(dd.serie_municipal_taxas['Município'])
indices_mun['Região'] = np.array(dd.serie_municipal_taxas['Região'])
indices_mun['Região'] = indices_mun['Região'].replace([1, 2, 3, 4], ['Baixada Fluminense', 'Rio de Janeiro', 'Grande Niterói', 'Interior'])
indices_mun['Data'] = np.array(dd.serie_municipal_taxas['Data'])
indices_mun.columns = ['Índice', 'Município', 'Região', 'Data']
indices_mun = indices_mun.groupby('Data')

### Criação do índice de criminalidade para o Estado:

#### Excluindo colunas desnecessárias para o índice:
set_crimes = dd.serie_estadual_taxas.drop(['Data', 'Ano', 'Mês', 'Homicídio por Intervenção Policial', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos',  'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências'], axis=1)

set_crimes = np.array(set_crimes)
set_crimes = pd.DataFrame(set_crimes, dtype=float)

set_crimes.columns = ['Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Total de Roubos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Ameaças']

#### Criando índice de criminalidade:

array_average_est = np.array(set_crimes)
indices_est = np.average(array_average_est, weights = penas_criminais['Pena média'], axis=1)
indices_est = pd.DataFrame(indices_est)
indices_est['Data'] = np.array(dd.serie_estadual_taxas['Data'])
indices_est.columns = ['Índice', 'Data']

## Criação dos índices agregados: Lesões e Letalidades, Roubos, Furtos e Outros:

### Município:

smt_mun_grupos = pd.DataFrame()
smt_mun_grupos['Município'] = np.array(dd.serie_municipal_taxas['Município'])
smt_mun_grupos['Região'] = np.array(dd.serie_municipal_taxas['Região'])
smt_mun_grupos['Região'] = smt_mun_grupos['Região'].replace([1, 2, 3, 4], ['Baixada Fluminense', 'Rio de Janeiro', 'Grande Niterói', 'Interior'])
smt_mun_grupos['Data'] = np.array(dd.serie_municipal_taxas['Data'])
smt_mun_grupos['Lesões e Letalidades'] = array_average_mun[:, :8].sum(axis=1)
smt_mun_grupos['Roubos'] = array_average_mun[:, 8]
smt_mun_grupos['Furtos'] = array_average_mun[:, 9]
smt_mun_grupos['Outros'] = array_average_mun[:, 10:].sum(axis=1)
indices_agregados_mun = smt_mun_grupos.groupby('Data')

### Estado:

indices_agregados_est = pd.DataFrame()
indices_agregados_est['Data'] = np.array(dd.serie_estadual_taxas['Data'])
indices_agregados_est['Lesões e Letalidades'] = array_average_est[:, :8].sum(axis=1)
indices_agregados_est['Roubos'] = array_average_est[:, 8]
indices_agregados_est['Furtos'] = array_average_est[:, 9]
indices_agregados_est['Outros'] = array_average_est[:, 10:].sum(axis=1)

# Importando layer do limite territorial:

mapeamento = gspd.read_file('mapeamento.dbf')
mapeamento = gspd.read_file('mapeamento.shp')
mapeamento = gspd.read_file('mapeamento.shx')

# Função para plotagem do mapa gráfico:

def plot_map(m,y):
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(indices_mun.get_group(date)['Índice'].reset_index())
    return(complet_map.plot(column='Índice', cmap='OrRd', legend=True, figsize=(18,9)))

def plot_map_rm(m,y):
    date = '{}/{}'.format(y,m)
    complet_map = mapeamento.join(indices_mun.get_group(date)['Índice'].reset_index())
    complet_map = complet_map.drop(['index'], axis=1)
    complet_map = complet_map.join(indices_mun.get_group(date)['Região'].reset_index())
    complet_map = complet_map[complet_map['Região'] != 'Interior']
    return(complet_map.plot(column='Índice', cmap='OrRd', legend=True, figsize=(18,9)))
