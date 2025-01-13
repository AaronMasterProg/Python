# Conjetura de Collatz
# 1. toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# 2. si es par, evalúa un nuevo c0 como c0 ÷ 2;
# 3. de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# 4. si c0 ≠ 1, salta al punto 2.

c0 = int(input("Ingrese un número entero positivo : "))
pasos=0
if c0 > 0:
    while c0 != 1:
        if c0 % 2:  
            c0 = c0 * 3 + 1
            pasos+=1
        else:
            c0 //= 2
            pasos+=1
            print(c0)
else:
    print("El numero no es valido.")
print("El numero de pasos es: ",pasos)
