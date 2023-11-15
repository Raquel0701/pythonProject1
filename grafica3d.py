import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Crear una gráfica en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot de los datos
ax.scatter(X[:, 0], X[:, 1], Y, c='blue', marker='o', label='Datos reales')

# Crear una cuadrícula 2D para las predicciones
x_min, x_max = X[:, 0].min(), X[:, 0].max()
y_min, y_max = X[:, 1].min(), X[:, 1].max()
x_surf, y_surf = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

# Predicciones en la cuadrícula
z_surf = modelo.predict(np.c_[x_surf.ravel(), y_surf.ravel()]).reshape(x_surf.shape)

# Superficie de la regresión lineal
ax.plot_surface(x_surf, y_surf, z_surf, color='green', alpha=0.5, label='Regresión Lineal')

# Etiquetas
ax.set_xlabel('Gestión del Cambio')
ax.set_ylabel('Liderazgo')
ax.set_zlabel('Cultura Organizacional')

# Leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
