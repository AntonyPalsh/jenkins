from json import loads 
from kafka import KafkaConsumer 
import sys
from clickhouse_driver import Client

import clickhouse_connect

my_consumer = KafkaConsumer( 
    'testnum', 
     bootstrap_servers = [sys.argv[1] + ':9092'], 
     auto_offset_reset = 'earliest', 
     enable_auto_commit = True, 
     group_id = 'my-group', 
     value_deserializer = lambda x : loads(x.decode('utf-8')) 
) 

for message in my_consumer: 
    message = message.value 
    #collection.insert_one(message) 
    #print(message + " added") 

client = Client(sys.argv[2]) #Set address clickhouse server
#result = client.execute("INSERT INTO db_superset.facts (*) VALUES (1, 'product 1', '2021-10-01', 'Customer 1', 10)")

client.execute("CREATE TABLE IF NOT EXISTS db_superset.facts (id UInt32, bid String, number Float32) ENGINE = Log;")



#print(result)