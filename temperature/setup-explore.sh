# Temperature data collector project notes

# load modules for GPIO and thermometer
sudo modprobe w1-gpio
sudo modprobe w1-therm

# view temperature sensor details
cd /sys/bus/w1/devices
ls  # <-- the DS18B20 should be listed in this directory...
cd 28-xxxx # <-- directory here with serial number
cat w1_slave # <-- not sure what this will show...