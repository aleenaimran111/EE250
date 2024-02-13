"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code " + str(rc))

if __name__ == '__main__':
    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Create a client object
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

    # Attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    # Connect to the MQTT broker
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

    # Ask paho-mqtt to spawn a separate thread to handle incoming and outgoing mqtt messages
    client.loop_start()
    time.sleep(1)

    while True:
        # Replace "user" with your USC username in all subscriptions
        client.publish("aleenaim/ipinfo/ip", f"{ip_address}")
        print("Publishing ip address")
        time.sleep(4)

        # Get date and time
        current_datetime = datetime.now()

        # Publish date and time in their own topics
        client.publish("aleenaim/ipinfo/date", current_datetime.strftime("%Y-%m-%d"))
        client.publish("aleenaim/ipinfo/time", current_datetime.strftime("%H:%M:%S"))

        print("Publishing date:", current_datetime.strftime("%Y-%m-%d"))
        print("Publishing time:", current_datetime.strftime("%H:%M:%S"))

        # Adding a short sleep time for stability
        time.sleep(4)

