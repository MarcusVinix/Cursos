import time
import datetime

print("time.localtime()...: ", time.localtime())
time.sleep(2) #aguardando 2 segundos
print("time.asctime()...: ", time.asctime())

for segundo in range(4):
    time.sleep(1)
    print("%d Segundo" % segundo)

dataEHora = datetime.datetime(2018,9,19,23,21,50)

print("Data: ", dataEHora.date())
print("Hora: ", dataEHora.time())
