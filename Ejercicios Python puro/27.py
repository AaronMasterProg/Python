def bis(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

def meses(año, mes):
    if año < 1582 or mes < 1 or mes > 12:
        return None
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = dias[mes - 1]
    if mes == 2 and bis(año):
        res = 29
    return res

def dia_a(año, mes, dia):
    dias = 0
    for m in range(1, mes):
        md = meses(año, m)
        if md == None:
            return None
        dias += md
    md = meses(año, mes)
    if dia >= 1 and dia <= md:
        return dias + dia
    else:
        return None

print("El numero de dia es: ",dia_a(2000, 12, 31))
