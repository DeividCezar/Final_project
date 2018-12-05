import pandas as pd
import Taxas_de_crescimento as tc

# A seguinte função gera um DataFrame que contém as correlações entre as taxas de crescimento das quatro regiões, utilizando o índice indicado ao chamar a função. Potencialmente, essa função gera cinco DataFrame, um para cada tipo de índice.
def correlação(tipo):
    '''
    Opções: ['Índice de criminalidade', 'Roubos', 'Furtos', 'Lesões e Letalidades', 'Outros']. Para cada índice indicado, ela retorna um DataFrame com a correlação entre as taxas de crescimento do índice das quatro regiões.
    '''
    if tipo in ['Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']:
        
        # Rearrumando o DataFrame das taxas de crescimento para index Data e colunas Região:
        indices_regioes_taxa_contra_RIO = tc.taxa_de_crescimento(tipo)
        indices_regioes_taxa_contra_RIO.index = [indices_regioes_taxa_contra_RIO['Data'], indices_regioes_taxa_contra_RIO['Região']]
        indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.drop(['Data', 'Região'],axis=1)
        indices_regioes_taxa_contra_RIO_unstack = indices_regioes_taxa_contra_RIO.unstack()
    
        # Calculando a matriz correlação:
        correlação = indices_regioes_taxa_contra_RIO_unstack.corr(method='pearson')
        
    else:
        
        correlação = print('Opção inválida. Veja as opções (coloque as aspas): [{}, {}, {}, {}, {}]'.format('Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros'))
        
    return correlação