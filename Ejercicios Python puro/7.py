# Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:

# 3x3 - 2x2 + 3x - 1

# El resultado debe ser asignado a y.

# Cuando x=0, y=-1.0
x = 0
x = float(x)
y=((3*(x**3))-(2*(x**2))+(3*x)-1)
print("y =", y)

# Cuando x=1, y=3.0
x = 1
x = float(x)
y=((3*(x**3))-(2*(x**2))+(3*x)-1)
print("y =", y)

# Cuando x=-1, y=-9.0
x = -1
x = float(x)
y=((3*(x**3))-(2*(x**2))+(3*x)-1)
print("y =", y)
