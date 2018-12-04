import pandas as pd
import Taxas_de_crescimento as tc

# A seguinte função gera
def correlação(tipo):
    
    # Rearrumando o DataFrame das taxas de crescimento para index Data e colunas Região:
    indices_regioes_taxa_contra_RIO = tc.taxa_de_crescimento(tipo)
    indices_regioes_taxa_contra_RIO.index = [indices_regioes_taxa_contra_RIO['Data'], indices_regioes_taxa_contra_RIO['Região']]
    indices_regioes_taxa_contra_RIO = indices_regioes_taxa_contra_RIO.drop(['Data', 'Região'],axis=1)
    indices_regioes_taxa_contra_RIO_unstack = indices_regioes_taxa_contra_RIO.unstack()
    
    # 
    correlação = indices_regioes_taxa_contra_RIO_unstack.corr(method='pearson')
    return correlação