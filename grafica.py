import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
datos = pd.read_excel("datos.xlsx")

# Definir las variables independientes (X) y la variable dependiente (Y)
X = datos[["Gestión del Cambio", "Liderazgo"]].values
Y = datos["Cultura Organizacional"].values

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
modelo.fit(X, Y)

# Imprimir los coeficientes
print("Intercepto:", modelo.intercept_)
print("Coeficientes:", modelo.coef_)

# Hacer una predicción
nuevos_datos = pd.DataFrame({"Gestión del Cambio": [4.5], "Liderazgo": [4.6]})
prediccion = modelo.predict(nuevos_datos)
print("Predicción:", prediccion[0])

# Crear una gráfica de dispersión
plt.scatter(X[:, 0], Y, label="Gestión del Cambio", color="blue")
plt.scatter(X[:, 1], Y, label="Liderazgo", color="red")

# Agregar la línea de regresión
plt.plot(X, modelo.predict(X), label="Regresión Lineal", color="green")

# Etiquetas y leyenda
plt.xlabel("Variables Independientes")
plt.ylabel("Cultura Organizacional")
plt.legend()

# Mostrar la gráfica
plt.show()
