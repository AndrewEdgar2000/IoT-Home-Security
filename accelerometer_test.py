from sense_hat import SenseHat
import time

sense = SenseHat()
alert = False
initial = sense.get_accelerometer_raw()

initialX = initial['x']
initialY = initial['y']
initialZ = initial['z']

initialXRounded = round(initialX,3)
initialYRounded = round(initialY,3)
initialZRounded = round(initialZ,3)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x,3)
    y = round(y,3)
    z = round(z,3)

    outputX = round(x - initialX, 3)
    outputY = round(x - initialY, 3)
    outputZ = round(x - initialZ, 3)
    
    #print("x ={0} y = {1} z={2}".format(x,y,z))

    #print("x = " + str(outputX))
    #print("y = " + str(outputY))

    if(outputX < -0.50 or outputX > 0.50):
        #print would be data sent to mqtt
        #can send outputX as data which represents the change from initial state
        #sent an alert as input for alarm
        print("HA I FOUND YOU!")
        alert = True
    elif(outputX < -0.30 or outputX > 0.30):
            print("someone there?"
    elif (outputX < -0.05 or outputX > 0.05):
            print("hmm must have been the wind")  

    if(outputY < -0.30 or outputY > 0.30):
        #print would be data sent to mqtt
        #can send outputX as data which represents the change from initial state
        print("HA I FOUND YOU! Y")
        alert = True
    elif(outputY < -0.30 or outputY > 0.30):
            print("someone there?")
    elif (outputY < -0.05 or outputY > 0.05):
            print("hmm must have been the wind")

    time.sleep(0.5)

    
