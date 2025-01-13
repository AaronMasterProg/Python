import numpy as np

# Función para calcular la entropía cruzada
def cross_entropy(p, q):
    p = np.array(p)
    q = np.array(q)
    return -np.sum(p * np.log(q))

# Ejemplo 1: Predicción buena
p = [0, 1]  # Etiqueta verdadera
q_good = [0.1, 0.9]  # Predicción buena

# Ejemplo 2: Predicción mala
q_bad = [0.8, 0.2]  # Predicción mala

# Cálculo de entropía cruzada
loss_good = cross_entropy(p, q_good)
loss_bad = cross_entropy(p, q_bad)

print(loss_good, loss_bad)
