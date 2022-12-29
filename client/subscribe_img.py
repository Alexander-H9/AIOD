import time
import paho.mqtt.client as mqtt
import sys
import argparse
import os

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings

from connection import Connection

# MQTT Subscriber

# password authentiacation: http://www.steves-internet-guide.com/mqtt-username-password-example/

parser = argparse.ArgumentParser()
#parser.add_argument('-p', dest='port', help='specify target host', required=False, type=int)
parser.add_argument('-u', dest='username', help='specify client username', required=False, type=str)
parser.add_argument('-pw', dest='password', help='specify client password', required=False, type=str)
args = parser.parse_args()
#port = args.port
username = args.username
password = args.password

#if port == None or port > 9 or port < 0: port = 1
if username == None: username = "alex"
if password == None: password = "aaap"


def on_connect(client, userdata, flags, rc):
    
    if rc == 5: 
        print("Authentication error")
        exit()

    print("Connected with result code "+str(rc))
    client.subscribe(f"rec_result/{port}/topic")
    print(f"Connected to topic rec_result/{port}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode('utf-8'))   # .decode('utf-8)

    erg = msg.payload.decode('utf-8')
    erg = erg.replace("[", "")
    erg = erg.replace("]", "")
    erg = erg.replace("(", "")
    erg = erg.replace(")", "")
    erg = erg.replace("'", "")
    erg = erg.split(",")

    obj = erg[1]
    per = erg[2]

    print(f'Server respons: \nObject:    {obj} \nPercentage: {per}')

    Connection.res = f'Object: {obj} \nPercentage: {round(float(per), 2)}'

    client.loop_stop()
    


def start_connection(username, password, p):
    global port
    port = p
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username=username, password=password)

    if client.connect(settings.adress.lokal_broker) != 0:        #)1883, 60
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)

    #try:
    # client.loop_forever()
    client.loop_start()
    time.sleep(1.0)

        # client.loop_end()
    #except:
    print("Disconnecting from broker")

    client.disconnect()

    return Connection.res



if __name__ == "__main__":

    # port = 1
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username=username, password=password)
    start_connection(client)