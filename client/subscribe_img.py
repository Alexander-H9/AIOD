import paho.mqtt.client as mqtt
import sys
import argparse
import os

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings
from gui_interface import authentication

# MQTT Subscriber

# password authentiacation: http://www.steves-internet-guide.com/mqtt-username-password-example/

parser = argparse.ArgumentParser()
parser.add_argument('-p', dest='port', help='specify target host', required=False, type=int)
parser.add_argument('-u', dest='username', help='specify client username', required=False, type=str)
parser.add_argument('-pw', dest='password', help='specify client password', required=False, type=str)
args = parser.parse_args()
port = args.port
username = args.username
password = args.password

if port == None or port > 9 or port < 0: port = 1
if username == None: username = "alex"
if password == None: password = "aaap"


def on_connect(client, userdata, flags, rc):

    if rc == 5: 
        print("Authentication error")
        authentication(False)
        exit()


    print("Connected with result code "+str(rc))
    client.subscribe(f"rec_result/{port}/topic")
    print(f"Connected to topic rec_result/{port}")
    authentication(True)


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
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username=username, password=password)

if client.connect(settings.adress.broker) != 0:        #)1883, 60
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)


#try:
print("Press CTRL + C to exit...")
client.loop_forever()

    # client.loop_end()
#except:
print("Disconnecting from broker")

client.disconnect()