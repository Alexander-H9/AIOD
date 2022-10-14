import paho.mqtt.client as mqtt
import sys

from object_detection import run
# from config import settings


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("send_img/topic")
    print("Listening to topic: send_img/topic")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)

    if type(msg.payload) == bytes:
        receive(msg)
    res = run()
    client.publish("rec_result/topic", str(res))
    print("Sent result")


def receive(msg):
    with open("server/media/output.jpg", "wb") as f:
        f.write(msg.payload)
    # maybe dont save the image, give the byte array to the ai instead
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


if client.connect("172.19.0.2", 1883, 60) != 0: 
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

try:
    print("Press CTRL + C to exit...")
    client.loop_forever()
except:
    print("Disconnecting from broker")

client.disconnect()