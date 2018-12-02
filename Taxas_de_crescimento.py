import pandas as pd
import numpy as np
import Índice as ind
#import geopandas as gspd

# Criação das taxas de crescimento da criminalidade baseadas nos índices criados

## Criação das taxas de crescimento da criminalidade nos municípios com relação ao Rio de Janeiro com base no índice de criminalidade:

### Transformei o DataFrame indices_mun em um array de uma coluna (indices_mun_array), adiantei um mês (indices_mun_array_adiantado)
### e subtraí o primeiro (somente até o penúltimo mês) do segundo e dividi para o primeiro excluído os zeros
### (indices_mun_array_sem_zeros: veja a observação abaixo), criando assim a taxa de crescimento da criminalidade em cada município
### considerando o índice de criminalidade baseado nas penas criminais (indices_mun_array_taxa_de_crescimento).
### Obs: (aso algum município não tenha registrado nenhum crime em um determinado mês) para evitar a divisão por zero,
### substituimos cada 0 por 1, de modo que a taxa de crescimento dessa exceção (mês, ano e município) seja exatamente
### o índice de criminalidade do mês seguinte:
indices_mun_array = np.array(ind.indices_mun)[:,0].reshape(5152,1)
indices_mun_array_sem_zeros = np.array(ind.indices_mun.replace(0,1))[:,0].reshape(5152,1)
indices_mun_array_adiantado = indices_mun_array[92:]
indices_mun_array_taxa_de_crescimento = (indices_mun_array_adiantado - indices_mun_array[:5060])/indices_mun_array_sem_zeros[:5060]

### Agora, transformo o resultado em um array cujas colunas são as datas e as linhas são os municípios e subtraio de cada linha as taxas de
### crescimento do município do Rio de Janeiro (município linha 67), criando assim um array (indices_mun_array_taxa_contra_RIO) que possui a
### taxa de crescimento de cada município com relação ao município do Rio de Janeiro:
indices_mun_array_taxa_de_crescimento_mesXmunicipio = indices_mun_array_taxa_de_crescimento.reshape(55,92).transpose()
indices_mun_array_taxa_contra_RIO = indices_mun_array_taxa_de_crescimento_mesXmunicipio - indices_mun_array_taxa_de_crescimento_mesXmunicipio[67]
indices_mun_array_taxa_contra_RIO = np.concatenate((np.zeros(92).reshape(92,1), indices_mun_array_taxa_contra_RIO), axis = 1)
indices_mun_array_taxa_contra_RIO = indices_mun_array_taxa_contra_RIO.transpose().reshape(5152,1)

### Criação do DataFrame do array resultante acima, transformando no formato original de indices_mun:
indices_mun_taxa_contra_RIO = pd.DataFrame(indices_mun_array_taxa_contra_RIO)
indices_mun_taxa_contra_RIO.columns = ['Taxa de crescimento do índice contra a capital']
indices_mun_taxa_contra_RIO['Município'] = ind.indices_mun['Município']
indices_mun_taxa_contra_RIO['Região'] = ind.indices_mun['Região']
indices_mun_taxa_contra_RIO['Data'] = ind.indices_mun['Data']

### Agrupamento por Data:
#indices_mun_taxa_contra_RIO = indices_mun_taxa_contra_RIO.groupby('Data')

## Criação das taxas de crescimento da criminalidade nos municípios com relação ao Rio de Janeiro com base nos índices agregados:

### Taxas de crescimento contra o RIO: criei uma função que nos dá o DataFrame das taxas de crescimento contra o RIO para cada um
### dos tipos de crimes agregados

def taxa_de_crescimento_agregada_contra_RIO(tipo):
    
    # taxa de crescimento
    indices_agregados_mun_array = np.array(ind.smt_mun_grupos[tipo]).reshape(5152,1)
    indices_agregados_mun_array_sem_zeros = np.array(ind.smt_mun_grupos[tipo].replace(0,1)).reshape(5152,1)
    indices_agregados_mun_array_adiantado = indices_agregados_mun_array[92:]
    indices_agregados_mun_array_taxa_de_crescimento = (indices_agregados_mun_array_adiantado - indices_agregados_mun_array[:5060])/indices_agregados_mun_array_sem_zeros[:5060]
    
    #taxa de crescimento contra RIO
    indices_agregados_array_mesXmun = indices_agregados_mun_array_taxa_de_crescimento.reshape(55,92).transpose()
    indices_agregados_array_contra_RIO = indices_agregados_array_mesXmun - indices_agregados_array_mesXmun[67]
    indices_agregados_array_contra_RIO = np.concatenate((np.zeros(92).reshape(92,1), indices_agregados_array_contra_RIO), axis = 1)
    indices_agregados_array_contra_RIO = indices_agregados_array_contra_RIO.transpose().reshape(5152,1)
    
    #Criação do DataFrame do array resultante acima, transformando no formato original de indices_mun:
    indices_agregados_contra_RIO = pd.DataFrame(indices_agregados_array_contra_RIO)
    indices_agregados_contra_RIO.columns = ['Taxa de crescimento de {} contra a capital'.format(tipo)]
    indices_agregados_contra_RIO['Munícipio'] = ind.indices_mun['Município']
    indices_agregados_contra_RIO['Região'] = ind.indices_mun['Região']
    indices_agregados_contra_RIO['Data'] = ind.indices_mun['Data']
    
    return indices_agregados_contra_RIO