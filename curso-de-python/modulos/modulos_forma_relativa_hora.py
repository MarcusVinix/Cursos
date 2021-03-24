from datetime import datetime

horaAgora = datetime.now()
hora = horaAgora.hour
minuto = horaAgora.minute
segundo = horaAgora.second

print(hora)
print(minuto)
print(segundo)
horaCompleta = hora, ":", minuto, ":", segundo
print(horaCompleta)
#10:35:45
print(str(hora)+":"+str(minuto)+":"+str(segundo))

print("%d:%d:%d" % (hora, minuto, segundo))