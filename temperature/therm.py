#!/usr/bin/python
# Program Description:
# This is a python script designed to run on a Raspberry Pi.  It takes a
# temperature reading from a DS18B20 sensor about once per second, and writes
# a datetime string and temperature to ./temps.csv
#
# Change variable 'rt' to have the program run for a different amount of time.
#
# Most of this code came directly from the tutorial at adafruit.com
# Visit http://tinyurl.com/o46z5pu for their example.
#
# I have modified their code to stop after a number of iterations
# and to output to a file with datetime values.  I am only writing the
# Celsius values for simplicity.
#
# Ben Rehberg
# Two Leg Software
# twoleg.com
#

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

rt = 24 # run-time, in hours
rtm = rt*60*60  # run-time in seconds

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

temps = open('temps.csv','w')   # open file for writing temp and time values
for x in range(0,rtm):
        t = time.localtime()
        temp = str(read_temp())
        tString = '{}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
        temps.write(tString + ', ' + temp + '\n')
        temps.flush()   #flush the buffer so we don't lose data if interrupted while running
        time.sleep(0.8) #read_temp() has sleep(0.2) so sleeping 0.8 here makes each iteration closer to 1 second

temps.close()