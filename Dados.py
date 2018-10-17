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


serie_estadual_taxas = pd.read_excel("Dados_taxas.xlsx")

serie_estadual_taxas = serie_estadual_taxas.drop("pol_militares_mortos_serv", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("pol_civis_mortos_serv", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("fase", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("prisoes", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("apf_cmp", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("apreensoes", axis=1)
serie_estadual_taxas = serie_estadual_taxas.drop("aaapai_cmba", axis=1)


serie_municipal = pd.read_excel("Dados_Municipio.xlsx")

serie_municipal = serie_municipal.drop("fmun_cod", axis=1)
serie_municipal = serie_municipal.drop("mes_ano", axis=1)
serie_municipal = serie_municipal.drop("apf_cmp", axis=1)
serie_municipal = serie_municipal.drop("aaapai_cmba", axis=1)
serie_municipal = serie_municipal.drop("pol_militares_mortos_serv", axis=1)
serie_municipal = serie_municipal.drop("pol_civis_mortos_serv", axis=1)
serie_municipal = serie_municipal.drop("fase", axis=1)

populacao_municipal = pd.read_excel("PopulaçãoMunicipal.xlsm")

populacao_municipal = populacao_municipal.drop("cod_munic", axis = 1)
populacao_municipal = populacao_municipal[2013 < populacao_municipal.vano]
populacao_municipal = populacao_municipal[2019 > populacao_municipal.vano]

serie_estadual.columns = ['Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estrupo', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_estadual.index = [serie_estadual['Ano'], serie_estadual['Mês']]
serie_estadual = serie_estadual.drop('Ano', axis = 1)
serie_estadual = serie_estadual.drop('Mês', axis = 1)

serie_estadual_taxas.columns = ['Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estrupo', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_estadual_taxas.index = [serie_estadual_taxas['Ano'], serie_estadual_taxas['Mês']]
serie_estadual_taxas = serie_estadual_taxas.drop('Ano', axis = 1)
serie_estadual_taxas = serie_estadual_taxas.drop('Mês', axis = 1)

serie_municipal.columns = ['Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estrupo', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_municipal.index = [serie_municipal['Ano'], serie_municipal['Mês']]

populacao_municipal.columns = ['Município', 'População do Município', 'Ano']
populacao_municipal.index = [populacao_municipal['Ano'], populacao_municipal['Município']]
populacao_municipal = populacao_municipal.drop('Ano', axis = 1)
populacao_municipal = populacao_municipal.drop('Município', axis = 1)

a = np.array(populacao_municipal['População do Município']).reshape(92,5)
a = a.transpose()
b = list(a[0])*12 + list(a[1])*12 + list(a[2])*12 + list(a[3])*12 + list(a[4])*8
b = np.ceil(np.array(b))

c = np.array(serie_municipal)
g = np.array(c[:,3]).reshape(5152,1)
e = c[:, 4:]
e = e.T
e = (e/b)*100000
e = e.T
e = np.concatenate((g, e), axis=1)

serie_municipal_taxas = pd.DataFrame(e)
serie_municipal_taxas.columns = ['Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estrupo', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
serie_municipal_taxas.index = [serie_municipal['Ano'], serie_municipal['Mês']]

serie_municipal = serie_municipal.drop('Ano', axis=1)
serie_municipal = serie_municipal.drop('Mês', axis=1)