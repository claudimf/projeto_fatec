import machine
from api import API
from get_timestamp import Time_Stamp


API().send_read(20, Time_Stamp().get_timestamp())
