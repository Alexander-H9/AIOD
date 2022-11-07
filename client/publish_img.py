import paho.mqtt.client as mqtt
import sys
import os
import argparse

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings

# MQTT Publusher

parser = argparse.ArgumentParser()
parser.add_argument('-p', dest='port', help='specify target host', required=False, type=int)
parser.add_argument('-u', dest='username', help='specify client username', required=False, type=str)
parser.add_argument('-pw', dest='password', help='specify client password', required=False, type=str)
args = parser.parse_args()
port = args.port
username = args.username
password = args.password

if port == None or port > 9 or port < 0: port = 1
if username == None: username = "alex"  # andreas
if password == None: password = "aaap"  # maekathon2022
# add new user password from passwd file: mosquitto_passwd -U passwd


def on_connect(client, userdata, flags, rc):

    if rc == 5: 
        print("Authentication error")
        exit()

    print("Connected with result code "+str(rc))


def get_picture_as_bytearray():
    img_path = os.path.join('../','server', 'media', 'basketball1.jpg')

    with open(img_path, "rb") as f:
        fileContent = f.read()

    byteArr = bytearray(fileContent)
    return byteArr


client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(username=username, password=password)

if client.connect("172.19.0.1", 1883, 60) != 0: 
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.publish(f"send_img/{port}/topic", get_picture_as_bytearray())


print(f'Client adress: {settings.adress.client}')
print(f'Broker adress: {settings.adress.broker}')

client.disconnect()

