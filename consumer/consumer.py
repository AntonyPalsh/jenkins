from json import loads 
from kafka import KafkaConsumer 
import sys
import clickhouse_connect
import time

print(sys.argv[1])
print(sys.argv[2])

my_consumer = KafkaConsumer( 
    'testnum', 
     bootstrap_servers = [sys.argv[1] + ':9092'], 
     auto_offset_reset = 'earliest', 
     enable_auto_commit = True, 
     group_id = 'my-group', 
     value_deserializer = lambda x : loads(x.decode('utf-8')) 
)

client = clickhouse_connect.get_client(host=sys.argv[2], username='default', password='password')
client.command('CREATE TABLE new_table (key UInt32, bid String, number Float64) ENGINE MergeTree ORDER BY key')

for message in my_consumer: 
    message = message.value 
    #collection.insert_one(message) 
    #print(message + " added") 

time.sleep(3600)