import machine
from api import API
from machine import RTC


rtc = RTC()
clock = rtc.datetime()
date = '%02u/%02u/%02u'%(clock[2],clock[1],clock[0])
time = '%02u:%02u:%02u'%(clock[4],clock[5],clock[6])
time_stamp = date + " " + time + " -0300"

API().send_read(20, time_stamp)
