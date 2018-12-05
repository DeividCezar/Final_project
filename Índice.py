import pandas as pd
import numpy as np
import Dados as dd
import altair as alt

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
indices_mun.columns = ['Índice']
indices_mun['Município'] = np.array(dd.serie_municipal_taxas['Município'])
indices_mun['Região'] = np.array(dd.serie_municipal_taxas['Região'])
indices_mun['Região'] = indices_mun['Região'].replace([1, 2, 3, 4], ['Baixada Fluminense', 'Rio de Janeiro', 'Grande Niterói', 'Interior'])
indices_mun['Data'] = np.array(dd.serie_municipal_taxas['Data'])
indices_municipio = indices_mun.groupby('Data')

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