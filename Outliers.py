import pandas as pd
import numpy as np
import Dados as dd

def todos_outliers():
    
    serie = input('Dados Estaduais ou Municipais? ')
    dados = input('Valores Absolutos ou Taxas? ')
    if serie == 'Municipais':
        munic = str(input('Escolha o Município: '))
    else:
        ano = int(input('Escolha o ano: '))
        
    def outliers(x):
        if serie == 'Estaduais':

            def outliers_iqr_estadual(ys):
                quartile_1, quartile_3 = np.percentile(ys.get_group(ano).iloc[:, x], [25, 75])
                iqr = quartile_3 - quartile_1
                lower_bound = quartile_1 - (iqr * 1.5)
                upper_bound = quartile_3 + (iqr * 1.5)
                return np.where((ys.get_group(ano).iloc[:, x] > upper_bound) | (ys.get_group(ano).iloc[:, x] < lower_bound))

            if dados == 'Absolutos':

                out = outliers_iqr_estadual(dd.grupo_ano_se)[0]
                a = dd.grupo_ano_se.get_group(ano)
                b = np.array(a)
                
                data_outlier = []
                if out != []:
                    for i in out:
                        data_outlier.append(b[i, 0])
                else:
                    data_outlier = 'o'

            elif dados == 'Taxas':

                out = outliers_iqr_estadual(dd.grupo_ano_set)[0]
                a = dd.grupo_ano_set.get_group(ano)
                b = np.array(a)
                
                data_outlier = []
                if out != []:
                    for i in out:
                        data_outlier.append(b[i, 0])
                else:
                    data_outlier = 'o'


        elif serie == 'Municipais':

            def outliers_iqr_municipal(ys):

                quartile_1, quartile_3 = np.percentile(ys.get_group(munic).iloc[:, x], [25, 75])
                iqr = quartile_3 - quartile_1
                lower_bound = quartile_1 - (iqr * 1.5)
                upper_bound = quartile_3 + (iqr * 1.5)
                return np.where((ys.get_group(munic).iloc[:, x] > upper_bound) | (ys.get_group(munic).iloc[:, x] < lower_bound))
            
            if dados == 'Absolutos':

                out = outliers_iqr_municipal(dd.grupo_mun_ano_sm)[0]
                a = dd.grupo_mun_ano_sm.get_group(munic)
                b = np.array(a)
                
                data_outlier = []
                if out != []:
                    for i in out:
                        data_outlier.append(b[i, 0])
                else:
                    data_outlier = 'o'

            elif dados == 'Taxas':

                out = outliers_iqr_municipal(dd.grupo_mun_ano_smt)[0]
                a = dd.grupo_mun_ano_smt.get_group(munic)
                b = np.array(a)
                
                data_outlier = []
                if out != []:
                    for i in out:
                        data_outlier.append(b[i, 0])
                else:
                    data_outlier = 'o'

        return data_outlier
    
    c = []
    for i in list(range(3, 44)):
        c.append(tuple(outliers(i)))
    
    c = np.array(c).reshape(1,41)
    c = pd.DataFrame(c)
    c.columns = ['Homicídio Doloso', 'Lesão Corporal seguida de Morte', 'Latrocínio', 'Homicídio por Intervenção Policial', 'Tentativa de Homicídio', 'Lesão Corporal Dolosa', 'Estupro', 'Homicídio Culposo', 'Lesão Corporal Culposa', 'Roubo a Comércio', 'Roubo a Residência', 'Roubo de Veículo', 'Roubo de Carga', 'Roubo a Transeunte', 'Roubo em Coletivo', 'Roubo a Banco', 'Roubo a Caixa Eletrônico', 'Roubo de Celular', 'Roubo com Condução para Saque', 'Roubo a Bicicleta', 'Outros Roubos', 'Total de Roubos', 'Furto de Veículos', 'Furto de Bicicleta', 'Outros Furtos', 'Total de Furtos', 'Sequestro', 'Extorsão', 'Sequestro Relâmpago', 'Estelionato', 'Apreensão de Drogas', 'Recuperação de Veículos', 'Cumprimento de Mandado de Prisão', 'Ameaças', 'Pessoas Desaparecidas', 'Encontro de Cadáver', 'Encontro de Ossada', 'Indicador de Letalidade', 'Indicador de Roubo na Rua', 'Indicador de Roubo de Veículos', 'Registro de Ocorrências']
    return c
pd.options.display.max_columns = 50