import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import tkinter as tk
from tkinter.colorchooser import askcolor

# Datos de ejemplo (RGB y nombre del color)
colores = np.array([[255, 0, 0],  # Rojo
                    [0, 255, 0],  # Verde
                    [0, 0, 255],  # Azul
                    [255, 255, 0],  # Amarillo
                    [0, 255, 255],  # Cian
                    [255, 0, 255]])  # Magenta

etiquetas = np.array([0, 1, 2, 3, 4, 5])  # 0: Rojo, 1: Verde, etc.

# Crear el modelo secuencial
modelo = Sequential()
modelo.add(Input(shape=(3,)))# En las nuevas versiones de Keras asi se emplea la entrada de datos, en este caso 3 neuronas o nodos de datos
modelo.add(Dense(5, activation='relu'))  # Agrega la capa oculta
modelo.add(Dense(6, activation='softmax'))  # Salida con 6 posibles colores
modelo.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(colores, etiquetas, epochs=500, verbose=False)

# Función para predecir el color seleccionado
def predecir_color(rgb):
    prediccion = modelo.predict(np.array([rgb]))
    etiqueta_predicha = np.argmax(prediccion)  # Obtener la etiqueta con mayor probabilidad
    colores_nombres = ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Cian', 'Magenta']
    return colores_nombres[etiqueta_predicha]

# Función para abrir el selector de color
def seleccionar_color():
    color = askcolor()[0]  # Abre el selector de color y obtiene el valor RGB
    if color:
        # Convertir el color a una lista con los valores RGB
        rgb = [int(color[0]), int(color[1]), int(color[2])]
        resultado = predecir_color(rgb)
        print(f'El color RGB {rgb} es {resultado}')
        etiqueta_resultado.config(text=f'El color seleccionado es: {resultado}')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Selector de Color")

# Botón para seleccionar el color
boton_seleccionar = tk.Button(ventana, text="Seleccionar color", command=seleccionar_color)
boton_seleccionar.pack(pady=20)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="El color seleccionado es: ", font=('Arial', 14))
etiqueta_resultado.pack(pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()

