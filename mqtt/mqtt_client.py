import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reasonCode, properties):
    print(f"Connected to EMQX with result code {reasonCode}")
    client.subscribe("your/topic")

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}, Message: {msg.payload.decode()}")

mqtt_client = mqtt.Client(protocol=mqtt.MQTTv5)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

def connect_broker(broker_url, port):
    mqtt_client.connect(broker_url, port, 60)
    mqtt_client.loop_start()
