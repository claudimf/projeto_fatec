# import upip
# upip.install('urequests')
import machine
import json
import urequests as requests
from get_variables import Enviroment_Variables
from network_connection import Network_Connection


class API:
    def send_read(self, temperature, time_stamp):
        if Network_Connection().conecta():
            host = Enviroment_Variables().get_variable('host')
            action = Enviroment_Variables().get_variable('action')
            url = host + "/" + action
            headers = {'Content-type': 'application/json; charset=UTF-8'}
            data = {}
            data['temperature'] = temperature
            data['time_stamp'] = time_stamp
            data = json.dumps(data)
            print("Data:" + data)
            print("URL:" + url)
            print("Headers:" + str(headers))
            response = requests.get(url, data=data, headers=headers)
            results = response.json()
            print(results)
            return response
        else:
            return False
