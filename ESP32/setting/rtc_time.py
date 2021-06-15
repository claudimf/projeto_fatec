import machine
import time
from machine import RTC


rtc = RTC()
rtc.datetime((2021, 5, 11, 0, 15, 51, 0, 0)) # (ano, mês, dia, dia da semana, hora, minuto, segundo, microsegundo)
while True:
    relogio = rtc.datetime()
    print('Data: %02u/%02u/%02u'%(relogio[2],relogio[1],relogio[0]))
    print('Hora: %02u:%02u:%02u'%(relogio[4],relogio[5],relogio[6]))
    time.sleep(1)
