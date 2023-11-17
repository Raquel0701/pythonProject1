# Regresión Lineal en Python

Este proyecto muestra cómo realizar una regresión lineal en Python utilizando las bibliotecas `pandas` y `scikit-learn`. En este ejemplo, se realiza una regresión lineal con "Cultura Organizacional" como variable dependiente (Y) y "Gestión del Cambio" y "Liderazgo" como variables independientes (X).

## Dependencias

Asegúrate de tener instaladas las siguientes bibliotecas en tu entorno de Python:

- [`pandas`](https://pandas.pydata.org/): Para trabajar con datos en formato de tabla.

- [`scikit-learn`](https://scikit-learn.org/stable/): Para realizar la regresión lineal.

- [`matplotlib`](https://matplotlib.org/): Para la visualización de gráficas.

Puedes instalar estas bibliotecas con los siguientes comandos en tu terminal:

```bash
pip install pandas scikit-learn matplotlib openpyxl
```


y ejecutar (Intercept, Coeficientes, Predicción)

```bash
python index.py 

```
y ejecutar (Gráfica 2D )

```bash
python grafica.py 

```
y ejecutar (Gráfica 3D )

```bash
python grafica3d.py 

```


## Regresión Lineal

En este proyecto, utilizamos la regresión lineal para analizar la relación entre las variables "Cultura Organizacional" y las variables independientes "Gestión del Cambio" y "Liderazgo". La regresión lineal es una técnica estadística que se utiliza para modelar la relación lineal entre una variable dependiente (Y) y una o más variables independientes (X).

### Conceptos clave

- **Variable Dependiente (Y)**: En nuestro caso, "Cultura Organizacional" es la variable que queremos predecir o explicar. Representa la respuesta o resultado que estamos interesados en analizar.

- **Variables Independientes (X)**: "Gestión del Cambio" y "Liderazgo" son las variables independientes que utilizamos para predecir la variable dependiente "Cultura Organizacional".

- **Intercepto**: El intercepto (coeficiente independiente) es el valor en el que la línea de regresión corta el eje Y cuando todas las variables independientes son cero.

- **Coeficientes**: Los coeficientes de regresión representan la relación entre las variables independientes y la variable dependiente. En nuestro caso, los coeficientes indican cuánto cambia "Cultura Organizacional" en respuesta a un cambio en "Gestión del Cambio" y "Liderazgo".

### Uso del modelo

Una vez que hemos ajustado el modelo de regresión lineal a nuestros datos, podemos usarlo para hacer predicciones sobre la variable dependiente. El modelo nos proporciona una ecuación que se puede utilizar para estimar "Cultura Organizacional" en función de los valores de "Gestión del Cambio" y "Liderazgo".

### Interpretación de los coeficientes

- El intercepto representa el valor esperado de "Cultura Organizacional" cuando "Gestión del Cambio" y "Liderazgo" son cero.

- El coeficiente de "Gestión del Cambio" (1.1499 en nuestro ejemplo) indica cuánto se espera que cambie "Cultura Organizacional" por cada unidad de cambio en "Gestión del Cambio", manteniendo constante "Liderazgo".

- El coeficiente de "Liderazgo" (-0.9735 en nuestro ejemplo) indica cuánto se espera que cambie "Cultura Organizacional" por cada unidad de cambio en "Liderazgo", manteniendo constante "Gestión del Cambio".

Estos coeficientes nos permiten entender cómo las variables independientes influyen en la variable dependiente en nuestro modelo de regresión lineal.

### Referencias adicionales

Para obtener más información sobre regresión lineal y su aplicación en Python, puedes consultar la documentación de scikit-learn: [Documentación de scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)

