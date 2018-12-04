import Taxas_de_crescimento as tc
import altair as alt
alt.renderers.enable('notebook')

# A seguinte função plota um gráfico de linhas mostrando a evolução da taxa de crescimento acima para cada uma das quatro regiões:
def plot_taxa_de_crescimento(tipo): 
    
    if tipo in ['Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']:
        
        highlight = alt.selection(type='single', on='mouseover', fields=['Região'], nearest=True) # Destaque gráfico para a linha mais próxima
        
        # Eixo y e Título condicionais ao tipo enviado 
        if tipo == 'Índice de criminalidade':
            Column = 'Taxa de crescimento da criminalidade'
            Title = 'Taxa de crescimento da criminalidade das quatro regiões'
        else:
            Column = 'Taxa de crescimento de {}'.format(tipo)
            Title = 'Taxa de crescimento de {} das quatro regiões'.format(tipo)
    
        # Plot
        taxa = alt.Chart(tc.taxa_de_crescimento('{}'.format(tipo))).encode(
            x = 'Data',
            y = Column,
            color = 'Região:N'
        )

        points = taxa.mark_circle().encode(
            opacity=alt.value(0)
        ).add_selection(
            highlight
        ).properties(
            width=800,
            height=200,
            title = Title
        ).interactive()

        lines = taxa.mark_line().encode(
            size=alt.condition(~highlight, alt.value(1), alt.value(4))
        )
        
        plot = points + lines

    else:
        
        plot = print('Opção inválida. Veja as opções (coloque as aspas): [{}, {}, {}, {}, {}]'.format('Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros'))
    
    return plot

# A seguinte função plota um gráfico de linhas mostrando a evolução da taxa de crescimento relativo acima para cada uma das quatro regiões:
def plot_taxa_de_crescimento_relativo(tipo): 
    
    if tipo in ['Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros']:
        
        highlight = alt.selection(type='single', on='mouseover', fields=['Região'], nearest=True) # Destaque gráfico para a linha mais próxima
        
        # Eixo y e Título condicionais ao tipo enviado 
        if tipo == 'Índice de criminalidade':
            Column = 'Taxa de crescimento relativo da criminalidade'
            Title = 'Taxa de crescimento relativo da criminalidade das quatro regiões com relação à capital Rio de Janeiro'
        else:
            Column = 'Taxa de crescimento relativo de {}'.format(tipo)
            Title = 'Taxa de crescimento relativo de {} das quatro regiões com relação à capital Rio de Janeiro'.format(tipo)
    
        # Plot
        taxa_contra_RIO = alt.Chart(tc.taxa_de_crescimento_relativo('{}'.format(tipo))).encode(
            x = 'Data',
            y = Column,
            color = 'Região:N'
        )

        points = taxa_contra_RIO.mark_circle().encode(
            opacity=alt.value(0)
        ).add_selection(
            highlight
        ).properties(
            width=800,
            height=200,
            title = Title
        ).interactive()

        lines = taxa_contra_RIO.mark_line().encode(
            size=alt.condition(~highlight, alt.value(1), alt.value(4))
        )
        
        plot = points + lines

    else:
        
        plot = print('Opção inválida. Veja as opções (coloque as aspas): [{}, {}, {}, {}, {}]'.format('Índice de criminalidade', 'Lesões e Letalidades', 'Roubos', 'Furtos', 'Outros'))
    
    return plot