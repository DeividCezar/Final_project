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

array_average = np.array(smt_mun)
indices = np.average(array_average, weights = penas_criminais['Pena média'], axis = 1)
indices = pd.DataFrame(indices)
indices['Município'] = np.array(dd.serie_municipal_taxas['Município'])
indices['Região'] = np.array(dd.serie_municipal_taxas['Região'])
indices['Região'] = indices['Região'].replace([1, 2, 3, 4], ['Baixada Fluminense', 'Rio de Janeiro', 'Grande Niterói', 'Interior'])
indices['Data'] = np.array(dd.serie_municipal_taxas['Data'])
indices.columns = ['Índice', 'Município', 'Região', 'Data']
indices = indices.groupby('Data')