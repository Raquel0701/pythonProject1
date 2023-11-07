import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de entrada
X = np.array([
    [4.10, 4.40, 4.20],
    [4.73, 4.85, 4.95],
    [3.43, 3.51, 3.69],
    [2.87, 4.28, 3.94],
    [3.48, 3.82, 3.86]
])

# Resultados
Y = np.array([4.20, 4.95, 3.69, 3.94, 3.86])

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
modelo.fit(X, Y)

# Imprimir los coeficientes
print("Intercepto:", modelo.intercept_)
print("Coeficientes:", modelo.coef_)

# Hacer una predicción
nuevos_datos = np.array([[4.5, 4.6, 4.4]])  # Ingresa tus propios valores de entrada
prediccion = modelo.predict(nuevos_datos)
print("Predicción:", prediccion)
