import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
 
serie = pd.read_excel('Dados_Estado.xlsx', header=0, parse_dates=[0], index_col=0, squeeze=True)
serie_e = series.hom_doloso
valores = serie_e.values
size = int(len(valores) * 0.66)
train, test = valores[0:size], valores[size:len(valores)]
history = [x for x in train]
previsao = list()
for t in range(len(test)):
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    previsao.append(yhat)
    obs = test[t]
    history.append(obs)
    print('previsto=%f, esperado=%f' % (yhat, obs))