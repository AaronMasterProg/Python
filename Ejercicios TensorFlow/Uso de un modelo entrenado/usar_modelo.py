import tensorflow as tf
import numpy as np
import os
import platform

#Este es el modelo entrenado del ejemplo de ecuacion cuadratica por minimos cuadrados

i=1
while i==1:
    os.system("cls")
    # Cargar el modelo guardado
    modelo_cargado = tf.keras.models.load_model('modelo_cuadratico.h5')

    # Hacer predicciones con el modelo cargado
    nuevos_valores_x = np.array([float(input("Carga un valor para evaluar: "))])  # Valores nuevos de entrada
    predicciones = modelo_cargado.predict(nuevos_valores_x)

    # Mostrar las predicciones
    for i in range(len(nuevos_valores_x)):
        print(f"x = {nuevos_valores_x[i]}, Predicción = {predicciones[i][0]}")

    i=int(input("¿Desea evaluar otro dato? 1/0: "))

    if i<=0:
        i==0
        print("Hasta luego")
    else:
        i==1
