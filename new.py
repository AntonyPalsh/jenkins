import random
import time
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer( 
    bootstrap_servers = ['localhost:9092'],
    value_serializer = lambda x:dumps(x).encode('utf-8') 
    ) 

for i in range(1, 51):
    time.sleep(0.1)
    #numbe = "bid_" + str(i) + ": " + str(random.uniform(0, (i*10)))
    data = {"bid_" + str(i) : str(random.uniform(0, (i*10)))}
    producer.send('mytopic', data)
    #print(numbe)