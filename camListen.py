#!/usr/bin/python

import paho.mqtt.client as mqtt
import time
import ssl
import os
import time
import subprocess

host          = "node02.myqtthub.com"
port          = 1883
clean_session = True
client_id     = "dropoutsCamera"
user_name     = "dropoutsCamera"
password      = "Edinburgh12"

def on_connect (client, userdata, flags, rc):
    """ Callback called when connection/reconnection is detected """
    print ("Connect %s result is: %s" % (host, rc))
    
    # With Paho, always subscribe at on_connect (if you want to
    # subscribe) to ensure you resubscribe if connection is
    # lost.
    # client.subscribe("some/topic")

    if rc == 0:
        client.connected_flag = True
        print ("connected OK")
        return
    
    print ("Failed to connect to %s, error was, rc=%s" % rc)
    # handle error here
    sys.exit (-1)


def on_message(client, userdata, msg):
    """ Callback called for every PUBLISH received """
    print("got a message")
    print ("%s => %s" % (msg.topic, str(msg.payload.decode("UTF-8"))))
    if str(msg.payload.decode("UTF-8")) == "1":
        print("Starting webcam for 10 seconds")
        subprocess.Popen('sudo /opt/webcam_streamer/start', shell=True)
        time.sleep(10)
        subprocess.Popen('pkill start', shell=True)
        #subprocess.Popen('pkill start')
        subprocess.Popen('pkill hawkeye', shell=True)

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
client.loop_start()

client.connected_flag = False
while not client.connected_flag:           #wait in loop
    client.loop()
    time.sleep (1)

client.subscribe("cameraControl")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()

# publish message (optionally configuring qos=1, qos=2 and retain=True/False)
#ret = client.publish ("some/message/to/publish", "{'status' : 'on'}")
#client.loop ()

#print ("Publish operation finished with ret=%s" % ret)

# close connection
#client.disconnect ()