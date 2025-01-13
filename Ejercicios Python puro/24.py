# Escenario
# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

for i in range(2):
    if i==0:
        member = input(f"Agrega al siguiente miembro: ")
        print(member," agregado")
        beatles.append(member)
    else:
        member = input(f"Agrega al siguiente miembro: ")
        beatles.append(member)
        print(member," agregado")

for _ in range(2):
        print("Eliminando a: ",beatles[-1])
        beatles.pop()

member="Ringo Starr"
beatles.insert(0,member)

print("Lista de los miembros de The Beatles actualizada", beatles)
print("Espera, ¿quien es Greg?")
