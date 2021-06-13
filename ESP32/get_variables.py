import ujson as json


class Enviroment_Variables:
    def get_variable(self, key):
        with open('variables.txt') as json_file:
            data = json.load(json_file)
            print(data[key])
        return data[key]
