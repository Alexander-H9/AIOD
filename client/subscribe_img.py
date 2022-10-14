import paho.mqtt.client as mqtt
import sys

# from config import settings

# MQTT Subscriber


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("rec_result/topic")
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

if client.connect("172.19.0.2") != 0:        #)1883, 60
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)


#try:
print("Press CTRL + C to exit...")
client.loop_forever()
    # client.loop_end()
#except:
print("Disconnecting from broker")

client.disconnect()