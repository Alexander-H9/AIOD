import paho.mqtt.client as mqtt
import sys
import os
import argparse
import time

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from object_detection import obj_det, init_obj_det
from text_recognition import text_recognition

# this functions dont work with the installed tf version
# from traffic_sign_detection import init_traffic_sign_det, traffic_sign_det # 
from config import settings

parser = argparse.ArgumentParser()
parser.add_argument('-u', dest='username', help='specify client username', required=False, type=str)
parser.add_argument('-pw', dest='password', help='specify client password', required=False, type=str)
args = parser.parse_args()
username = args.username
password = args.password

if username == None: username = "server"
if password == None: password = "server_pw"

global media_type
global connections
media_type = {}
connections = {}
ai_function = {}


def get_port():
    for p in range(1000,2001,1):
        if p not in connections:
            connections[p] = "conncected"
            return p


def on_connect(client, userdata, flags, rc):

    if rc == 5: 
        print("Authentication error")
        exit()

    print("Connected with result code "+str(rc))
    # topics to receive images and for authentication
    client.subscribe(f'authentication/topic')
    print("Listening to topic: authentication/topic...")
    print("Listening to topic: send_img/topic...")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic != f'authentication/topic':
        port = int(msg.topic.split("/")[1])
        print(f"topic: {msg.topic}, port: {port}")


    if msg.topic == f'authentication/topic':
        time.sleep(0.1)
        new_port = get_port()
        print(f'Starting authentication of port {new_port}')
        client.subscribe(f'function_topic/{new_port}/topic')
        client.subscribe(f'send_img/{new_port}/topic')
        client.subscribe(f'authentication/{new_port}/topic')
        client.subscribe(f'media_type/{new_port}/topic')
        client.subscribe(f'disconnect/{new_port}/topic')
        client.publish(f'auth_succ/topic', new_port)
        media_type[new_port] = "None"
        print("Authentication finished")

    elif msg.topic == f'function_topic/{port}/topic':
        ai_function[port] = msg.payload.decode('utf-8')

    elif msg.topic == f'media_type/{port}/topic':
        media_type[port] = msg.payload.decode('utf-8')

    elif msg.topic == f'send_img/{port}/topic':


        print(f'COMPUTING result for request by client {port}\nUsing {ai_function[port]}')
        receive(msg, media_type[port], port)
        
        if ai_function[port] == "object_detection":
            res = obj_det(model, media_type[port], port)

        elif ai_function[port] == "text_recognition":
            res = text_recognition(media_type[port], port)

        print("PUBLISH ", res, " to port ", port)
        client.publish(f'rec_result/{port}/topic', str(res))


    elif msg.topic == f'disconnect/{port}/topic':
        connections.pop(port)
        media_type.pop(port)
        ai_function.pop(port)
        print(f'CLIENT {port} is disconnectiong\nREMOVING occupied resources\nPORT {port} is available for a new connection')
        client.unsubscribe(f'send_img/{port}/topic')
        client.unsubscribe(f'authentication/{port}/topic')
        client.unsubscribe(f'media_type/{port}/topic')
        client.unsubscribe(f'function_topic/{port}/topic')
        client.unsubscribe(f'disconnect/{port}/topic')


def receive(msg, media_t, port):
    with open(f'/app/server/media/output_{port}.{media_t}', "wb") as f:
        f.write(msg.payload)
    # maybe dont save the image, give the byte array to the ai instead
    


if __name__ == '__main__':

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Starting ai server...")
    model = init_obj_det()
    # model_traffic = init_traffic_sign_det()
    print("done, models loaded and server is running")

    client.username_pw_set(username=username, password=password)

    if client.connect(settings.adress.broker) != 0:         # "172.19.0.2" , 1883, 60
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)

    #try:
    print("Press CTRL + C to exit...")
    client.loop_forever()
    #except:
    print("Disconnecting from broker")

    client.disconnect()