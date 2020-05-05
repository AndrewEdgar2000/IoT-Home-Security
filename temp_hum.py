from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
sense.clear()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white =(255,255,255)

def temperature():
    temp = sense.get_temperature()
    print(temp)
    if temp >34:
        sense.clear(red)
    elif temp< 34 and temp >24:
        sense.clear(green)
    elif temp <24 and temp > 0:
        sense.clear(blue)
    elif temp <0 and temp > -20:
        sense.clear(white)
    sleep(1)
    sense.show_message("The temperature is: " + str(round(temp,2)))
    return(temp)

def humidity():
    hum = sense.get_humidity()
    print(hum)
    if hum > 40:
        sense.clear(blue)
    elif hum< 40 and hum > 30:
        sense.clear(green)
    elif hum < 30 and hum > 0:
        sense.clear(red)
    sleep(1)
    sense.show_message("The humidity is: " + str(round(hum,2)))
    return(hum)

def pressure():
    pressure = sense.get_pressure()
    sense.show_message("The pressure in the room is: " + str(round(pressure , 2)))
    return(pressure)