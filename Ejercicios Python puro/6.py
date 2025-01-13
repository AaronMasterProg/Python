# Escenario
# Millas y kilómetros son unidades de longitud o distancia.

# Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

#  Millas a kilómetros;
#   Kilómetros a millas.

kilometers = 12.25
miles = 7.38

# Por regla de 3 se realizan las operaciones.

miles_to_kilometers = (miles*1.6)
kilometers_to_miles = (kilometers/1.6)

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
