# Importación de librerías necesarias
import tensorflow as tf  # Para la creación y entrenamiento de modelos de redes neuronales
import matplotlib.pyplot as plt  # Para graficar el progreso de la pérdida durante el entrenamiento
import numpy as np  # Para manejar arrays y realizar cálculos numéricos

# Datos de entrada: la ecuación 2x^2-4x-6
celsius = np.array([-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],dtype=float)  # Temperaturas en grados Celsius
farenheit = np.array([874,792,714,640,570,504,442,384,330,280,234,192,154,120,90,64,42,24,10,0,-6,-8,-6,0,10,24,42,64,90,120,154,192,234,280,330,384,442,504,570,640,714],dtype=float)  # Temperaturas equivalentes en grados Fahrenheit

# Definición de la capa de la red neuronal, 3 capas ocultas, con 80 neuronas cada una, ademas de utiliza la funcion de activación relu
# ReLU es una función de activación que permite activar o desactivar una neurona si esta ya no tiene un aprendizaje significativo

capa1 = tf.keras.layers.Dense(units=80, input_shape=[1], activation='relu')
capa2 = tf.keras.layers.Dense(units=80,activation='relu')
capa3 = tf.keras.layers.Dense(units=80,activation='relu')
salida = tf.keras.layers.Dense(units=1) # capa de salida

# Creación del modelo secuencial con las capas definidas
modelo = tf.keras.Sequential([capa1,capa2,capa3,salida])

# Compilación del modelo:
# Se usa el optimizador Adam con una tasa de aprendizaje de 0.1
# La función de pérdida utilizada es error cuadrático medio, que es común en problemas donde la función es lineal, es decir, una entrada a una salida
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),  # Optimización usando Adam con tasa de aprendizaje de 0.1
    loss='mean_squared_error' # Función de pérdida: error cuadrático medio
)

# Mensaje para indicar que comienza el entrenamiento
print("Entrenamiento...")

# Entrenamiento del modelo: 
# El modelo se entrena por 3000 épocas, utilizando los datos de entrada y salida que son las tabulaciones de la ecuación
# 'verbose=False' significa que no se imprimen detalles durante el entrenamiento
historial = modelo.fit(celsius, farenheit, epochs=3000, verbose=False)

# Mensaje para indicar que el modelo ha sido entrenado
print("Modelo entrenado")

# Graficar el progreso de la pérdida a lo largo de las épocas de entrenamiento
plt.xlabel("# Epoca")  # Etiqueta del eje X: número de épocas
plt.ylabel("Magnitud de perdida")  # Etiqueta del eje Y: magnitud de la pérdida (error)
plt.plot(historial.history["loss"])  # Graficar la pérdida registrada en el historial

# Mostrar el gráfico
plt.show()

print("Predicción")

# El modelo hace una predicción para un valor de entrada de 22 y -22
resultado = modelo.predict(np.array([22]))
resultado1 = modelo.predict(np.array([-22]))

# Imprimir el resultado de la predicción
print(f"El resultado es {str(resultado)}")
print(f"El resultado1 es {str(resultado1)}")

# Guardar el modelo entrenado
modelo.save('modelo_cuadratico.h5')


