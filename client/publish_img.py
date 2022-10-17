import paho.mqtt.client as mqtt
import sys
import os

# from config import settings

# MQTT Publusher

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def get_picture_as_bytearray():
    img_path = os.path.join('../','server', 'media', 'basketball1.jpg')

    with open(img_path, "rb") as f:
        fileContent = f.read()

    byteArr = bytearray(fileContent)
    return byteArr


client = mqtt.Client()
client.on_connect = on_connect


if client.connect("172.19.0.2", 1883, 60) != 0: 
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.publish("send_img/topic", get_picture_as_bytearray())

client.disconnect()

