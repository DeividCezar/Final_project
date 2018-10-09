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

serie_estadual_taxas.columns = ['Ano', 'Mês', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estrupo', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

serie_municipal.columns = ['Município', 'Ano', 'Mês', 'Região', 'Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estrupo', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']

populacao_municipal.index = range(populacao_municipal.shape[0])
populacao_municipal.columns = ['Município', 'População do Município', 'Ano']