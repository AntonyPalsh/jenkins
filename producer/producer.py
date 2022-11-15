import random
import time
import sys
from kafka import KafkaProducer
from json import dumps

print(sys.argv[1])

producer = KafkaProducer( 
    bootstrap_servers = [sys.argv[1] + ':9092'],
    value_serializer = lambda x:dumps(x).encode('utf-8') 
    ) 

for i in range(1, 51):
    time.sleep(0.1)
    numbe = "bid_" + str(i) + ": " + str(random.uniform(0, (i*10)))
    data = {"bid_" + str(i) : str(random.uniform(0, (i*10)))}
    producer.send('mytopic', data)
    print(numbe)

time.sleep(3600)