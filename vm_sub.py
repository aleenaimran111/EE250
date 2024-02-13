"""EE 250L Lab 04 Starter Code
Run vm_pub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code " + str(rc))
    client.subscribe("aleenaim/ipinfo/ip")
    client.subscribe("aleenaim/ipinfo/date")
    client.subscribe("aleenaim/ipinfo/time")

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_from_ipinfo(client, userdata, message):
    print("Custom callback - IP Message: " + message.payload.decode())

def on_ip_message(client, userdata, message):
    print("Custom callback - IP: " + message.payload.decode())

def on_date_message(client, userdata, message):
    print("Custom callback - Date: " + message.payload.decode())

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.on_message = on_message
    client.on_connect = on_connect

    # Adding custom callbacks for specific topics
    client.message_callback_add("aleenaim/ipinfo/ip", on_ip_message)
    client.message_callback_add("aleenaim/ipinfo/date", on_date_message)

    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    
    client.loop_forever()

