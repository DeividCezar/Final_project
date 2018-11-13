import pandas as pd
import numpy as np

# IMPORTAÇÃO E LIMPEZA DOS DADOS:

## Importação:

### Importação da série estadual (valores absolutos)
serie_estadual = pd.read_excel("Dados_Estado.xlsx")

### Importação da série estadual (taxas por 100 mil habitantes)
serie_estadual_taxas = pd.read_excel("Dados_taxas.xlsx")

### Importação da série municipal (valores absolutos)
serie_municipal = pd.read_excel("Dados_Municipio.xlsx")

### Importação da população municipal
populacao_municipal = pd.read_excel("PopulaçãoMunicipal.xlsm")

## Limpeza:

### Limpeza de serie_estadual:

#### Removendo colunas não interessantes para a análise (explicado no notebook 2):
serie_estadual = serie_estadual.drop(["pol_militares_mortos_serv", "pol_civis_mortos_serv", "fase", "prisoes", "apf_cmp", "apreensoes", "aaapai_cmba"], axis=1)

#### Limpeza de dados inexistentes, transformando ' ' em Not a Number por motivos de trababilidade:
ar_e = np.array(serie_estadual)
boolean_e = ar_e == ' '
ar_e[boolean_e] = np.nan
serie_estadual = pd.DataFrame(ar_e)
##### Observação: problemas com DataFrame type nos levaram a usar o Numpy aqui.

#### Criação da coluna Data:
Data = []
for i in list(range(1991, 2018)):
    
    for j in list(range(1, 10)):
        Data.append('{}/0{}'.format(i, j))
        
    for j in list(range(10, 13)):
        Data.append('{}/{}'.format(i, j))
        
for j in list(range(1, 9)):
    Data.append('2018/0{}'.format(j))
    
Data = np.array(Data).reshape(332,1)
    
se = np.array(serie_estadual)
se = np.concatenate((Data, se), axis = 1)
serie_estadual = pd.DataFrame(se)

#### Renomeando as colunas adequadamente e Data com index:
serie_estadual.columns = ['Data', 'Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_estadual.index = serie_estadual['Data']
serie_estadual = serie_estadual.drop('Data', axis=1)

### Limpeza de serie_estadual_taxas:

#### Removendo colunas não interessantes para a análise:
serie_estadual_taxas = serie_estadual_taxas.drop(["pol_militares_mortos_serv", "pol_civis_mortos_serv", "fase", "prisoes", "apf_cmp", "apreensoes", "aaapai_cmba"], axis=1)

#### Limpeza de dados inexistentes, transformando ' -   ' em Not a Number por motivos de tratabilidade:
ar_et = np.array(serie_estadual_taxas)
boolean_et = ar_et == ' -   '
ar_et[boolean_et] = np.nan
serie_estadual_taxas = pd.DataFrame(ar_et)

#### Criação da coluna Data:
Data = []
for i in list(range(2003, 2018)):
    
    for j in list(range(1, 10)):
        Data.append('{}/0{}'.format(i, j))
        
    for j in list(range(10, 13)):
        Data.append('{}/{}'.format(i, j))
        
for j in list(range(1, 9)):
    Data.append('2018/0{}'.format(j))
    
Data = np.array(Data).reshape(188,1)
    
se_t = np.array(serie_estadual_taxas)
se_t = np.concatenate((Data, se_t), axis = 1)
serie_estadual_taxas = pd.DataFrame(se_t)

#### Renomeando as colunas adequadamente e Data como index:
serie_estadual_taxas.columns = ['Data', 'Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_estadual_taxas.index = serie_estadual_taxas['Data']
serie_estadual_taxas = serie_estadual_taxas.drop('Data', axis=1)

### Limpeza de serie_municipal:

#### Removendo colunas não interessantes para a análise:
serie_municipal = serie_municipal.drop(["fmun_cod", "mes_ano", "apf_cmp", "aaapai_cmba", "pol_militares_mortos_serv", "pol_civis_mortos_serv", "fase"], axis=1)

#### Limpeza de dados inexistentes, transformando ' ' em Not a Number por motivos de tratabilidade:
ar_m = np.array(serie_municipal)
boolean_m = ar_m == ' '
ar_m[boolean_m] = np.nan
serie_municipal = pd.DataFrame(ar_m)

#### Criação da coluna Data:
Data = []
for i in list(range(2014, 2018)):
    
    for j in list(range(1, 10)):
        
        for t in list(range(92)):
            Data.append('{}/0{}'.format(i, j))
        
    for j in list(range(10, 13)):
        
        for t in list(range(92)):
            Data.append('{}/{}'.format(i, j))
        
for j in list(range(1, 9)):
    
    for t in list(range(92)):
        Data.append('2018/0{}'.format(j))
    
Data = np.array(Data).reshape(5152,1)

sm = np.array(serie_municipal)
sm = np.concatenate((Data, sm), axis = 1)
serie_municipal = pd.DataFrame(sm)

#### Renomeando as colunas adequadamente e Data como index:
serie_municipal.columns = ['Data', 'Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_municipal.index = serie_municipal['Data']
serie_municipal = serie_municipal.drop('Data', axis=1)

### Limpeza de populacao_municipal

#### Removendo colunas e linhas não interessantes para a análise:
populacao_municipal = populacao_municipal.drop("cod_munic", axis = 1)
populacao_municipal = populacao_municipal[2013 < populacao_municipal.vano]
populacao_municipal = populacao_municipal[2019 > populacao_municipal.vano]

#### Renomeando as colunas adequadamente:
populacao_municipal.columns = ['Município', 'População do Município', 'Ano']

# CRIAÇÃO DAS TAXAS MUNICIPAIS POR 100 MIL HABITANTES:

## Tomando coluna com as populações de forma adequada ao formato da coluna Município de serie_municipal:
a = np.array(populacao_municipal['População do Município']).reshape(92,5)
a = a.transpose()
b = list(a[0])*12 + list(a[1])*12 + list(a[2])*12 + list(a[3])*12 + list(a[4])*8
b = np.ceil(np.array(b))

## Criação de um array contendo as taxas municipais no formato desejado e criando o DataFrame serie_municipal_taxas:
p = np.array([serie_municipal['Município'], serie_municipal['Ano'], serie_municipal['Mês'], serie_municipal['Região']]).T
c = np.array(serie_municipal)
e = c[:, 4:]
e = e.T
e = (e/b)*100000
e = e.T
e = np.concatenate((Data, p, e), axis=1)

serie_municipal_taxas = pd.DataFrame(e)

## Renomeando as colunas adequadamente e Data como index:
serie_municipal_taxas.columns = ['Data', 'Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

serie_municipal_taxas.index = serie_municipal_taxas['Data']
serie_municipal_taxas = serie_municipal_taxas.drop('Data', axis=1)