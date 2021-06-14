import dht
import time
from machine import Pin


class TemperatureSensor:
    def get_temperature(self):
        d = dht.DHT11(Pin(12))
            try:
                d.measure()
                temperature = d.temperature()
                print('Temperatura: %02.1f' %temperature)
                humidity = d.humidity()
                print('Umidade: %02.1f %%RH' %humidity)
                time.sleep(1)
            except OSError as err:
                print('Erro na leitura!')
                time.sleep(1)
        return temperature
