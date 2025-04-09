import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connection {reason_code}")
    client.subscribe("banana")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    utf = msg.payload.decode('utf-8')
    print(utf)
    if 'hello' in utf:
        mqttc.publish('banana', 'Hello back')

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("test.mosquitto.org", 1883, 60)
mqttc.publish("banana","banana")
mqttc.loop_forever()