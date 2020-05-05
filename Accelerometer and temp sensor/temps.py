from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
sense.clear()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white =(255,255,255)

def gettemperature():
    temp = sense.get_temperature()
    print("temperature" + str(temp))
    sleep(1)
    return(temp)

def gethumidity():
    hum = sense.get_humidity()
    print("humidity is " + str(hum))
    
    sleep(1)
    return(hum)

def getpressure():
    pressure = sense.get_pressure()
    print("pressure is" + str(pressure))
    return(pressure)
