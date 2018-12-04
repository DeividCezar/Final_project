import pandas as pd
import numpy as np

# IMPORTAÇÃO E LIMPEZA DOS DADOS:

## Importação:

### Importação da série municipal (valores absolutos)
serie_municipal = pd.read_excel("Dados_Municipio.xlsx")

### Importação da população municipal
populacao_municipal = pd.read_excel("PopulaçãoMunicipal.xlsm")

## Limpeza:

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
e = c[:, 5:]
e = e.T
e = (e/b)*100000
e = e.T
e = np.concatenate((Data, p, e), axis=1)

serie_municipal_taxas = pd.DataFrame(e)

## Renomeando as colunas adequadamente e Data como index:
serie_municipal_taxas.columns = ['Data', 'Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

serie_municipal_taxas.index = serie_municipal_taxas['Data']