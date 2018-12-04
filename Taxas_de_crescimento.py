import pandas as pd
import numpy as np
import Índice as ind
#import geopandas as gspd

# A seguinte função nos dá (um DataFrame com) a taxa de crescimento de uma variável de cada região:
def taxa_de_crescimento(tipo):
    
    if tipo == 'Índice de criminalidade':
        
        # gerando o índice de criminalidade por região:
        indices_regioes = ind.indices_mun.drop('Município', axis=1)
        indices_regioes = indices_regioes.groupby(['Data','Região']).mean()
        indices_regioes = indices_regioes.unstack()
        
        # criando a taxa de crescimento do índice de criminalidade para cada região:
        indices_regioes_array = np.array(indices_regioes)
        indices_regioes_array = indices_regioes_array.T
        indices_regioes_taxa_de_crescimento = (indices_regioes_array[:,1:]-indices_regioes_array[:,:55])/indices_regioes_array[:,:55]
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento*100
        indices_regioes_taxa_de_crescimento = np.concatenate((np.zeros(4).reshape(4,1), indices_regioes_taxa_de_crescimento), axis=1)
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento.T
        
        # organizando em um DataFrame:
        indices_regioes_taxa_de_crescimento = pd.DataFrame(indices_regioes_taxa_de_crescimento)
        indices_regioes_taxa_de_crescimento.columns = ['Baixada Fluminense', 'Grande Niterói', 'Interior', 'Rio de Janeiro']
        indices_regioes_taxa_de_crescimento.index = indices_regioes.index
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento.stack()
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento.reset_index()
        indices_regioes_taxa_de_crescimento.columns = ['Data', 'Região', 'Taxa de crescimento da criminalidade']
        
    elif tipo in ['Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']:
        
        # gerando o índice de criminalidade por região:
        indices_regioes = ind.smt_mun_grupos.drop('Município', axis=1)
        indices_regioes = indices_regioes.groupby(['Data','Região']).mean()
        indices_regioes = indices_regioes.unstack()
        
        # criando a taxa de crescimento do índice de criminalidade para cada região:
        indices_regioes_array = np.array(indices_regioes[tipo])
        indices_regioes_array = indices_regioes_array.T
        indices_regioes_taxa_de_crescimento = (indices_regioes_array[:,1:]-indices_regioes_array[:,:55])/indices_regioes_array[:,:55]
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento*100
        indices_regioes_taxa_de_crescimento = np.concatenate((np.zeros(4).reshape(4,1), indices_regioes_taxa_de_crescimento), axis=1)
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento.T
        
        # organizando em um DataFrame:
        indices_regioes_taxa_de_crescimento = pd.DataFrame(indices_regioes_taxa_de_crescimento)
        indices_regioes_taxa_de_crescimento.columns = ['Baixada Fluminense', 'Grande Niterói', 'Interior', 'Rio de Janeiro']
        indices_regioes_taxa_de_crescimento.index = indices_regioes.index
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento.stack()
        indices_regioes_taxa_de_crescimento = indices_regioes_taxa_de_crescimento.reset_index()
        indices_regioes_taxa_de_crescimento.columns = ['Data', 'Região', 'Taxa de crescimento de {}'.format(tipo)]
        
    else:
        
        indices_regioes_taxa_de_crescimento = print('Opção inválida. Veja as opções (coloque as aspas): [{}, {}, {}, {}, {}]'.format('Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros'))
        
    return indices_regioes_taxa_de_crescimento
       

# A seguinte função nos dá (um DataFrame com) a taxa de crescimento relativo (a diferença entre as taxas de crescimento de uma variável de 
# uma determinada região e as taxas de crescimento da mesma variável na capital Rio de Janeiro):
def taxa_de_crescimento_relativo(tipo):
    
    if tipo in ['Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']:
    
        # taxa de crescimento contra RIO:
        indices_regioes_taxa_contra_RIO = taxa_de_crescimento(tipo)
        indices_regioes_taxa_contra_RIO.index = [indices_regioes_taxa_contra_RIO['Data'], indices_regioes_taxa_contra_RIO['Região']]
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.drop(['Data', 'Região'],axis=1)
        indices_regioes_taxa_contra_RIO_unstack = indices_regioes_taxa_contra_RIO.unstack()
        indices_regioes_taxa_contra_RIO = np.array(indices_regioes_taxa_contra_RIO_unstack)
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.T
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO - indices_regioes_taxa_contra_RIO[3]
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.T
    
        # transformando em um DataFrame no formato adequado, com colunas Data, Região e Taxa de crescimento relativo da criminalidade:
        indices_regioes_taxa_contra_RIO = pd.DataFrame(indices_regioes_taxa_contra_RIO)
        indices_regioes_taxa_contra_RIO.columns = ['Baixada Fluminense', 'Grande Niterói', 'Interior', 'Rio de Janeiro']
        indices_regioes_taxa_contra_RIO.index = indices_regioes_taxa_contra_RIO_unstack.index
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.stack()
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.reset_index()
    
        if tipo == 'Índice de criminalidade':
        
            indices_regioes_taxa_contra_RIO.columns = ['Data', 'Região', 'Taxa de crescimento relativo da criminalidade']
        
        elif tipo in ['Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']:

            indices_regioes_taxa_contra_RIO.columns = ['Data', 'Região', 'Taxa de crescimento relativo de {}'.format(tipo)]
        
    else:
        
        indices_regioes_taxa_contra_RIO = print('Opção inválida. Veja as opções (coloque as aspas): [{}, {}, {}, {}, {}]'.format('Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros'))
    
    return indices_regioes_taxa_contra_RIO