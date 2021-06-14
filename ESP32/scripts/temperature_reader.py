import machine
from api import API
from get_timestamp import Time_Stamp
from get_temperature import TemperatureSensor


API().send_read(TemperatureSensor().get_temperature(), Time_Stamp().get_timestamp())
