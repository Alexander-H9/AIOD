import paho.mqtt.client as mqtt
import sys
from tensorflow.keras.preprocessing import image

# MQTT Subscriber

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/topic")
    print("Connected to topic test/topic")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))   # .decode('utf-8)

    if type(msg.payload) == bytes:
        receive(msg)



def receive(msg):
    with open("media/output.jpg", "wb") as f:
        f.write(msg.payload)
    # maybe dont save the image, give the byte array to the ai instead


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

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

