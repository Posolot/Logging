import time
import paho.mqtt.client as mqtt_client
import requests
from logger_config import setup_logger

logger = setup_logger('Subscriber')

broker = "broker.emqx.io"

def get_user_id():
    response = requests.get("http://127.0.0.1:8000/get_user_id")
    return response.json()['user_id']

user_id = get_user_id()
client = mqtt_client.Client(client_id=user_id, protocol=mqtt_client.MQTTv311)

logger.info(f"User ID for Subscriber: {user_id}")

def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.info(f"Received message: {data}")

client.on_message = on_message

logger.info("Connecting to broker")
client.connect(broker)
client.loop_start()
logger.info("Subscribing")
client.subscribe("lab/leds/state")

# Check if no messages are received within a certain period (e.g., 30 seconds)
timeout = time.time() + 30
while time.time() < timeout:
    time.sleep(1)

logger.warning("No messages received for 30 seconds")

client.disconnect()
client.loop_stop()
