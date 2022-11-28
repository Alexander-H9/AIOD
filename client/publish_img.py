import paho.mqtt.client as mqtt
import sys
import os
import argparse
import time

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings
from connection import Connection

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
if password == None: password = "aaap"  # makeathon2022
# add new user password from passwd file: mosquitto_passwd -U passwd


def on_connect(client, userdata, flags, rc):
    if rc == 5: 
        print("Authentication error")
        Connection.connection = False
    elif rc == 0:
        Connection.connection = True
    
    print("Connected with result code "+str(rc))


def get_picture_as_bytearray(img_path):
    # img_path = os.path.join('server', 'media', 'basketball1.jpg')

    with open(img_path, "rb") as f:
        fileContent = f.read()

    byteArr = bytearray(fileContent)
    return byteArr


def authenticate(client: mqtt.Client):
    """
    starts a connection to the mqtt broker

    Args:
        client
    Returns:
        authentication status
    """
    print("1")
    def on_disconnect(client, userdata, rc=0):
        print("Disconnected result code "+str(rc))
        client.loop_stop()
        # Connection.connection = False
        return Connection.connection

    def on_message(client: mqtt.Client, userdata, msg):
        """ wait for the auth msg from the server
        """
        print("6")
        if msg.topic == f'auth_succ/{port}/topic':
            print("7")
            print("Auth succ")
            Connection.connection = True
            client.disconnect()
    
    if client.connect(settings.adress.lokal_broker) != 0:
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)
    print("2")
    # subscribe to the auth topic from the server
    client.subscribe(f'auth_succ/{port}/topic')
    print("3")
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    # send the auth request
    print("4")
    client.publish(f"authentication/{port}/topic", "authentication")
    # wait for the response
    print("5")
    client.loop_start()
    time.sleep(1)
    
    # continue if successfull, else exit
    print("6")
    client.disconnect()

    return Connection.connection


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect

    client.username_pw_set(username=username, password=password)

    # if authenticate(client):
    #     print("auth done")
    # else:
    #     print("auth error")

    if client.connect(settings.adress.lokal_broker) != 0: 
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)

    print(f"send_img/{port}/topic")

    client.publish(f"send_img/{port}/topic", get_picture_as_bytearray("server/media/basketball1.jpg"))    # 

    client.disconnect()