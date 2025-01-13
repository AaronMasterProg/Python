# Escenario
# La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
minutos=mins+(hour*60)+dura
horas=minutos//60
horaf=horas%24
minf=minutos-(horas*60)

print("Tu hora de inicio es: "+str(hour)+":"+str(mins))
print("Tu hora de fin es:",horaf,":",minf)
