import paho.mqtt.client as mqtt
import sys

from server.object_detection import get_picture_as_bytearray
from config import settings

# MQTT Publusher

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print(settings.adress.broker)


if client.connect("172.19.0.2", 1883, 60) != 0: 
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)


client.publish("test/topic", "Hello, the following file will be an .jpg image as bytearray", 0)
client.publish("test/topic", get_picture_as_bytearray())

client.disconnect()