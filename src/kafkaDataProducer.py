from kafka import KafkaProducer
import random
import threading
import time
import uuid

peopleInGym = []


def sendKafkaMessage(value, key):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('gymetrics', value, key)
    producer.flush()


def sendEntryData():
    key = str(uuid.uuid4())
    userId = random.randint(10000, 30000)
    peopleInGym.append(userId)
    dataToSend = "%s, true, %s, %s" % (userId, time.ctime(),len(peopleInGym))
    nextSend = random.randint(0, 5)
    sendKafkaMessage(dataToSend.encode(), key.encode())
    threading.Timer(nextSend, sendEntryData).start()


def sendExitData():
    if len(peopleInGym) > 0:
        key = str(uuid.uuid4())
        randomIndex = random.randint(0, len(peopleInGym) - 1)
        userId = peopleInGym[randomIndex]
        peopleInGym.remove(userId)
        dataToSend = "%s, false, %s, %s" % (userId, time.ctime(), len(peopleInGym))
        sendKafkaMessage(dataToSend.encode(), key.encode())
    nextSend = random.randint(10, 30)
    threading.Timer(nextSend, sendExitData).start()


sendEntryData()
sendExitData()

