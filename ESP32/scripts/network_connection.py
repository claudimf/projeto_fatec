import machine
import network
import json
from get_variables import Enviroment_Variables


class Network_Connection:
    def conecta(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        network_name = Enviroment_Variables().get_variable('network_name')
        password = Enviroment_Variables().get_variable('password')
        if not wlan.isconnected():
            print('Conectando na rede...')
            wlan.connect(network_name, password)
            while not wlan.isconnected():
                pass

        print('Dados da rede:')
        rede = wlan.ifconfig()
        print('IP:' + str(rede[0]))
        print('Máscara de rede:' + str(rede[1]))
        print('Gateway:' + str(rede[2]))
        print('Servidor DNS:' + str(rede[3]))
        return wlan.isconnected()
