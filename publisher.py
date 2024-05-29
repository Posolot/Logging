import time
import paho.mqtt.client as mqtt_client
import random
import requests
from logger_config import setup_logger

logger = setup_logger('Publisher')

broker = "broker.emqx.io"

def get_user_id():
    response = requests.get("http://127.0.0.1:8000/get_user_id")
    return response.json()['user_id']

user_id = get_user_id()
client = mqtt_client.Client(client_id=user_id, protocol=mqtt_client.MQTTv311)

logger.info(f"User ID for Publisher: {user_id}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected to broker")
    else:
        logger.error("Connection failed with code {rc}")

client.on_connect = on_connect

logger.info("Connecting to broker")
client.connect(broker)
client.loop_start()
logger.info("Publishing")
