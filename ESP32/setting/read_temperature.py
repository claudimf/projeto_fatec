import dht
import time
from machine import Pin


d = dht.DHT11(Pin(12))
# d = dht.DHT22(Pin(12))
while True:
    try:
        d.measure()
        temperatura = d.temperature()
        print('Temperatura: %02.1f' %temperatura)
        umidade = d.humidity()
        print('Umidade: %02.1f %%RH' %umidade)
        time.sleep(1)
    except OSError as err:
        print('Erro na leitura!')
        time.sleep(1)
