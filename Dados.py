import pandas as pd
import numpy as np

serie_estadual = pd.read_excel("Dados_Estado.xlsx")

serie_estadual = serie_estadual.drop("pol_militares_mortos_serv", axis=1)
serie_estadual = serie_estadual.drop("pol_civis_mortos_serv", axis=1)
serie_estadual = serie_estadual.drop("fase", axis=1)
serie_estadual = serie_estadual.drop("prisoes", axis=1)
serie_estadual = serie_estadual.drop("apf_cmp", axis=1)
serie_estadual = serie_estadual.drop("apreensoes", axis=1)
serie_estadual = serie_estadual.drop("aaapai_cmba", axis=1)
ar_e = np.array(serie_estadual)
boolean_e = ar_e == ' '
ar_e[boolean_e] = np.nan
serie_estadual = pd.DataFrame(ar_e)

serie_estadual_taxas = pd.read_excel("Dados_taxas.xlsx")

serie_estadual_taxas = serie_estadual_taxas.drop("pol_militares_mortos_serv", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("pol_civis_mortos_serv", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("fase", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("prisoes", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("apf_cmp", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("apreensoes", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("aaapai_cmba", axis=1)
ar_et = np.array(serie_estadual_taxas)
boolean_et = ar_et == ' -   '
ar_et[boolean_et] = np.nan
serie_estadual_taxas = pd.DataFrame(ar_et)


serie_municipal = pd.read_excel("Dados_Municipio.xlsx")

serie_municipal = serie_municipal.drop("fmun_cod", axis=1)
serie_municipal = serie_municipal.drop("mes_ano", axis=1)
serie_municipal = serie_municipal.drop("apf_cmp", axis=1)
serie_municipal = serie_municipal.drop("aaapai_cmba", axis=1)
serie_municipal = serie_municipal.drop("pol_militares_mortos_serv", axis=1)
serie_municipal = serie_municipal.drop("pol_civis_mortos_serv", axis=1)
serie_municipal = serie_municipal.drop("fase", axis=1)
ar_m = np.array(serie_municipal)
boolean_m = ar_m == ' '
ar_m[boolean_m] = np.nan
serie_municipal = pd.DataFrame(ar_m)

populacao_municipal = pd.read_excel("PopulaçãoMunicipal.xlsm")

populacao_municipal = populacao_municipal.drop("cod_munic", axis = 1)
populacao_municipal = populacao_municipal[2013 < populacao_municipal.vano]
populacao_municipal = populacao_municipal[2019 > populacao_municipal.vano]

Data = []
for i in list(range(1991, 2018)):
    for j in list(range(1, 10)):
        Data.append('0{}/{}'.format(j, i))
    for j in list(range(10, 13)):
        Data.append('{}/{}'.format(j, i))
for j in list(range(1, 9)):
    Data.append('0{}/2018'.format(j))
Data = np.array(Data).reshape(332,1)
    
se = np.array(serie_estadual)
se = np.concatenate((Data, se), axis = 1)
serie_estadual = pd.DataFrame(se)

serie_estadual.columns = ['Data', 'Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

se_ano = serie_estadual[:]
se_ano.index = [se_ano['Mês']]
grupo_ano_se = se_ano.groupby('Ano')

se_mes = serie_estadual[:]
se_mes.index = [se_mes['Ano']]
grupo_mes_se = se_mes.groupby('Mês')

serie_estadual.index = serie_estadual['Data']
serie_estadual = serie_estadual.drop('Data', axis=1)

Data = []
for i in list(range(2003, 2018)):
    for j in list(range(1, 10)):
        Data.append('0{}/{}'.format(j, i))
    for j in list(range(10, 13)):
        Data.append('{}/{}'.format(j, i))
for j in list(range(1, 9)):
    Data.append('0{}/2018'.format(j))
Data = np.array(Data).reshape(188,1)
    
se_t = np.array(serie_estadual_taxas)
se_t = np.concatenate((Data, se_t), axis = 1)
serie_estadual_taxas = pd.DataFrame(se_t)

serie_estadual_taxas.columns = ['Data', 'Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

set_ano = serie_estadual_taxas[:]
set_ano.index = [set_ano['Mês']]
grupo_ano_set = set_ano.groupby('Ano')

set_mes = serie_estadual_taxas[:]
set_mes.index = [set_mes['Ano']]
grupo_mes_set = set_mes.groupby('Mês')

serie_estadual_taxas.index = serie_estadual_taxas['Data']
serie_estadual_taxas = serie_estadual_taxas.drop('Data', axis=1)

Data = []
for i in list(range(2014, 2018)):
    
    for j in list(range(1, 10)):
        
        for t in list(range(92)):
            Data.append('0{}/{}'.format(j, i))
        
    for j in list(range(10, 13)):
        
        for t in list(range(92)):
            Data.append('{}/{}'.format(j, i))
        
for j in list(range(1, 9)):
    
    for t in list(range(92)):
        Data.append('0{}/2018'.format(j))
    
Data = np.array(Data).reshape(5152,1)

sm = np.array(serie_municipal)
sm = np.concatenate((Data, sm), axis = 1)
serie_municipal = pd.DataFrame(sm)

serie_municipal.columns = ['Data', 'Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

sm_mun_ano = serie_municipal[:]
sm_mun_ano.index = [sm_mun_ano['Ano']]
grupo_mun_ano_sm = sm_mun_ano.groupby('Município')

sm_ano = serie_municipal[:]
sm_ano.index = [sm_ano['Mês']]
grupo_ano_sm = sm_ano.groupby('Ano')

sm_mes = serie_municipal[:]
sm_mes.index = [sm_mes['Ano']]
grupo_mes_sm = sm_mes.groupby('Mês')

serie_municipal.index = serie_municipal['Data']
serie_municipal = serie_municipal.drop('Data', axis=1)

populacao_municipal.columns = ['Município', 'População do Município', 'Ano']
populacao_municipal.index = [populacao_municipal['Ano'], populacao_municipal['Município']]
populacao_municipal = populacao_municipal.drop('Ano', axis = 1)
populacao_municipal = populacao_municipal.drop('Município', axis = 1)

a = np.array(populacao_municipal['População do Município']).reshape(92,5)
a = a.transpose()
b = list(a[0])*12 + list(a[1])*12 + list(a[2])*12 + list(a[3])*12 + list(a[4])*8
b = np.ceil(np.array(b))

Data = []
for i in list(range(2014, 2018)):
    
    for j in list(range(1, 10)):
        
        for t in list(range(92)):
            Data.append('0{}/{}'.format(j, i))
        
    for j in list(range(10, 13)):
        
        for t in list(range(92)):
            Data.append('{}/{}'.format(j, i))
        
for j in list(range(1, 9)):
    
    for t in list(range(92)):
        Data.append('0{}/2018'.format(j))
    
Data = np.array(Data).reshape(5152,1)

p = np.array([serie_municipal['Município'], serie_municipal['Ano'], serie_municipal['Mês'], serie_municipal['Região']]).T
c = np.array(serie_municipal)
e = c[:, 4:]
e = e.T
e = (e/b)*100000
e = e.T
e = np.concatenate((Data, p, e), axis=1)

serie_municipal_taxas = pd.DataFrame(e)
ar_mt = np.array(serie_municipal_taxas)
boolean_mt = ar_mt == ' -   '
ar_mt[boolean_mt] = np.nan
serie_municipal_taxas = pd.DataFrame(ar_mt)
serie_municipal_taxas.columns = ['Data', 'Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

smt_mun = serie_municipal_taxas.drop(['Data', 'Município', 'Ano', 'Mês', 'Homicídio por Intervenção Policial', 'Total de Roubos', 'Total de Furtos', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências'], axis=1)
smt_mun = np.array(smt_mun)
smt_mun = pd.DataFrame(smt_mun, dtype=float)
smt_mun.columns = ['Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Ameaças']
smt_mun['Município'] = serie_municipal_taxas['Município']
smt_mun['Data'] = serie_municipal_taxas['Data']
grupo = smt_mun.groupby('Município')
grupo_mun_mean = smt_mun.groupby('Município').mean()

smt_ano = serie_municipal_taxas[:]
smt_ano.index = [smt_ano['Mês']]
grupo_ano_smt = smt_ano.groupby('Ano')

smt_mes = serie_municipal_taxas[:]
smt_mes.index = [smt_mes['Ano']]
grupo_mes_smt = smt_mes.groupby('Mês')

smt_mun_ano = serie_municipal_taxas[:]
smt_mun_ano.index = [smt_mun_ano['Ano']]
grupo_mun_ano_smt = smt_mun_ano.groupby(smt_mun_ano['Município'])

serie_municipal_taxas.index = serie_municipal_taxas['Data']
serie_municipal_taxas = serie_municipal_taxas.drop('Data', axis=1)