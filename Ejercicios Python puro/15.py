# Escenario
# Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

# El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.

# Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.

year = int(input("Introduce un año: "))

if year < 1582:
        print("No esta dentro del período del calendario Gregoriano")
else:
    if year %4 != 0:
        print("Es un año común")
    elif year%100 != 0:
        print("Es un año bisiesto")
    elif year%400 != 0:
        print("Es un año común")
    else:
        print("Es un año bisiesto")
