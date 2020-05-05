
#Imports
import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import ssl
#connect to team mqtthub
host          = "node02.myqtthub.com"
port          = 1883
clean_session = True
client_id     = "accelerometer"
user_name     = "accelerometer"
password      = "Stirling35"

#check connection
def on_connect (client, userdata, flags, rc):
    """ Callback called when connection/reconnection is detected """
    print ("Connect %s result is: %s" % (host, rc))

    if rc == 0:
        client.connected_flag = True
        print ("connected OK")
        return
    
    print ("Failed to connect to %s, error was, rc=%s" % rc)
    # handle error here
    sys.exit (-1)

#input message
def on_message(client, userdata, msg):
    """ Callback called for every PUBLISH received """
    print ("%s => %s" % (msg.topi, str(msg.payload)))

# Define clientId, host, user and password
client = mqtt.Client (client_id = client_id, clean_session = clean_session)
client.username_pw_set (user_name, password)

client.on_connect = on_connect
client.on_message = on_message

# configure TLS connection
# client.tls_set (cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
# client.tls_insecure_set (False)
# port = 8883

# connect using standard unsecure MQTT with keepalive to 60
client.connect (host, port, keepalive = 60)
client.connected_flag = False
while not client.connected_flag:           #wait in loop
    client.loop()
    time.sleep (1)

# publish message (optionally configuring qos=1, qos=2 and retain=True/False)
client.subscribe("acceleration")
client.loop ()

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
        client.publish("pi test","Warning Concerning movement!!")
    elif(outputX < -0.30 or outputX > 0.30):
            print("someone there?")
            client.publish("pi test" ,"slight sudden movement")
    elif (outputX < -0.05 or outputX > 0.05):
            print("hmm must have been the wind")
            client.publish("pi test","slight movement")

    

    time.sleep(5)

#keyboard interrupt to break loop

# close connection
client.disconnect ()
