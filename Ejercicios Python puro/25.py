# Escenario
# Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new = []

for i  in my_list:
    if i not in new:
        new.append(i)

print("La lista con elementos únicos:")
print(new)
