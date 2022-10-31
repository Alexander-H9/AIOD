import paho.mqtt.client as mqtt
import sys
import argparse

# from config import settings

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
        exit()

    print("Connected with result code "+str(rc))
    print(userdata)
    

    client.subscribe(f"rec_result/{port}/topic")
    print("Connected to topic rec_result")


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

if client.connect("172.19.0.4") != 0:        #)1883, 60
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)


#try:
print("Press CTRL + C to exit...")
client.loop_forever()
    # client.loop_end()
#except:
print("Disconnecting from broker")

client.disconnect()