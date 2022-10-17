import paho.mqtt.client as mqtt
import sys
import os
# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from object_detection import obj_det, init_obj_det
from config import settings


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("send_img/topic")
    print("Listening to topic: send_img/topic")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
    receive(msg)
    res = obj_det(model)
    client.publish("rec_result/topic", str(res))


def receive(msg):
    with open("media/output.jpg", "wb") as f:
        f.write(msg.payload)
    # maybe dont save the image, give the byte array to the ai instead
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

model = init_obj_det()

print(settings.adress.client)
print(settings.adress.broker)

if client.connect("172.19.0.2") != 0:         # "172.19.0.2" , 1883, 60
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

#try:
print("Press CTRL + C to exit...")
client.loop_forever()
#except:
print("Disconnecting from broker")

client.disconnect()