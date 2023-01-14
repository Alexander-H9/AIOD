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
    print(f"Connected to topic rec_result/{port}")
    client.subscribe(f"rec_result/{port}/topic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode('utf-8'))   # .decode('utf-8)

    # if obj_detection (parsing msg):
    if msg.payload.decode('utf-8').startswith("["):
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
        Connection.res = obj

    # if text recognition and other
    else:
        Connection.res = msg.payload.decode('utf-8')

    if msg.payload.decode('utf-8') == "":
        Connection.res = "-"

    Connection.rec_flag = True
    


def start_connection(username, password, p, media_type, byte_img, ai_function="object_detection"):
    global port
    port = p
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username=username, password=password)

    if client.connect(settings.adress.broker) != 0:        #)1883, 60
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)

    # clean exit
    if media_type == 0 and byte_img == 0:
        client.publish(f'disconnect/{port}/topic', "Good bye")
        return 0

    client.loop_start()

    client.publish(f'function_topic/{port}/topic', ai_function)
    client.publish(f'media_type/{port}/topic', media_type)
    client.publish(f"send_img/{port}/topic", byte_img)

    timeout = 0
    while Connection.rec_flag == False:
        if timeout >= 250.0: 
            Connection.res = "timout for classification"
            break
            
        time.sleep(0.1)
        timeout += 1

    Connection.rec_flag = False
    
    return Connection.res



if __name__ == "__main__":

    # port = 1
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username=username, password=password)
    start_connection(client)