# Escenario 
# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

# Prueba tu código con los datos que hemos proporcionado.

blocks = int(input("Ingresa el número de bloques: "))
height = 0
total= 0

while blocks >= total + height + 1:
    height += 1
    total+= height

print("La altura de la pirámide con", blocks, "bloques es: ", height)




