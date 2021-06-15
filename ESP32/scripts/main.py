import machine
import time
from api import API
from get_timestamp import Time_Stamp
from get_temperature import TemperatureSensor


time_sleep = 2 # 2 seconds

while True:
    try:
        API().send_read(
                        TemperatureSensor().get_temperature(), 
                        Time_Stamp().get_timestamp()
                        )
        time.sleep(time_sleep)
    except OSError:
        print('Erro na leitura!')
        time.sleep(time_sleep)
