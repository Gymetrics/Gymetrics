import time
from flask import (
    Flask,
    request,
)

import requests

from kafka import KafkaConsumer


app = Flask(__name__)


def readtopic():
    consumer = KafkaConsumer('gymetrics', bootstrap_servers=['localhost:9092'])

    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                              message.offset, message.key,
                                            message.value.decode('utf-8')))

        payload = {
            "location_name": "Sky Gym",
            "number_of_people": message.value.decode('utf-8').split(",")[3]
        }


        requests.put("http://localhost:8000/api/gym", data=payload)


readtopic()
