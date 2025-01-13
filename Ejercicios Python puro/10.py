# Escenario
# Tu tarea es completar el código para poder evaluar la siguiente expresión:
# El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios.

# Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario). Prueba tu código cuidadosamente.

x = float(input("Ingresa el valor para x: "))

# Divide y vencerás, al ser una expresión larga, lo ideal será dividirlo en partes y evaluarlo así.

# Empieza de abajo para arriba.

primero=1/x
segundo=1/(x+primero)
tercero=1/(x+segundo)
y=1/(x+tercero)

# Y se muestra la salida de cuarto, que es el global de las operaciones o para el ejercicio: y

print("Este es tu resultado:"+str(y))

