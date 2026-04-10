from sklearn.linear_model import LinearRegression
import numpy as np

def prever_demanda(series):
    X = np.arange(len(series)).reshape(-1, 1)
    y = series.values
    model = LinearRegression()
    model.fit(X, y)
    next_step = model.predict([[len(series)]])
    return next_step[0]
