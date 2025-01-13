# Dando formato a la salida
# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

#Minimizar el número de invocaciones de la función print() insertvando \n en las cadenas.

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# Hacer que la flecha sea el doble de grande (pero mantener las proporciones)

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *   *\n  *   *\n  *   *\n  *   *\n  *   *\n  *****")

# Duplica la flecha, colocando ambas flechas una al lado de la otra.

print("    *         *")
print("   * *       * *")
print("  *   *     *   *")
print(" *     *   *     *")
print("***   *** ***   ***")
print("  *   *     *   *")
print("  *   *     *   *")
print("  *****     *****")

#elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?

print("    *         *")
print("   * *       * *")
print("  *   *     *   *")
print(" *     *   *     *")
print("***   *** ***   ***")
print("  *   *     *   *")
print("  *   *     *   *")
#print("  *****     *****)

# Se quita las comillas en la linea 40
#File "/home/colado15/Python1/./2.1.13LAB.py", line 40
#    print("  *****     ***** )
#                            ^ 
#                             SyntaxError: EOL while scanning string literal
#Como se puede notar para este error si acierta.

#Haz lo mismo con algunos de los parentesis.
print("    *         *")
print("   * *       * *")
print("  *   *     *   *")
print(" *     *   *     *")
print("***   *** ***   ***")
print("  *   *     *   *")
print("  *   *     *   *")
#print("  *****     *****"

# Se quita el parentesis en la linea 56

# File "/home/colado15/Python1/./2.1.13LAB.py", line 59
#             ^
#    SyntaxError: unexpected EOF while parsing

# cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?

#Print("Hola mundo")

# Traceback (most recent call last):
#  File "/home/colado15/Python1/./2.1.13LAB.py", line 67, in <module>
#      Print("Hola mundo")
#      NameError: name 'Print' is not defined

# El error indica que Print no esta definido, ya que no es el nombre correcto de nuestra función.

# reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.

print('    *         *')
print("   * *       * *")
print("  *   *     *   *")
print(" *     *   *     *")
print("***   *** ***   ***")
print("  *   *     *   *")
print("  *   *     *   *")
print("  *****     *****")

# Cuando se cambia por apostrofes, lo sigue detectando como una cadena de texto, entonces imprime sin problema.
