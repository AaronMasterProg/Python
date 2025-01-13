# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

def liters_100km_to_miles_gallon(litros):
    galones = litros / 3.785411784
    millas = 100 * 1000 / 1609.344
    return millas / galones

def miles_gallon_to_liters_100km(millas):
    kms = millas * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / kms

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
