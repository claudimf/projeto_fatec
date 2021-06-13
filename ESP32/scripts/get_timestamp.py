import machine
import time
from machine import RTC


class Time_Stamp:
    def get_timestamp(self):
        rtc = RTC()
        clock = rtc.datetime()
        date = '%02u/%02u/%02u'%(clock[2],clock[1],clock[0])
        time = '%02u:%02u:%02u'%(clock[4],clock[5],clock[6])
        time_stamp = date + " " + time + " -0300"
        return time_stamp
