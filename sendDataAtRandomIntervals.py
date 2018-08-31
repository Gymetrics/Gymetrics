import random
import threading
import time

usersInGym = []

def sendEntryData():
    userId = random.randint(10000,30000)
    usersInGym.append(userId)
    dataToSend = "%s, true, %s" % (userId, time.ctime())
    nextSend = random.randint(0,5)
    print dataToSend #replace this with producer send method
    threading.Timer(nextSend, sendEntryData).start()
 
def sendExitData():
    if len(usersInGym) > 0:
        randomIndex = random.randint(0, len(usersInGym) - 1)
        userId = usersInGym[randomIndex]
        usersInGym.remove(userId)
        dataToSend = "%s, false, %s" % (userId, time.ctime())
        nextSend = random.randint(0,5)
        print dataToSend #replace this with producer send method
        threading.Timer(nextSend, sendExitData).start()
     
sendEntryData() 
sendExitData()
   
   
    
