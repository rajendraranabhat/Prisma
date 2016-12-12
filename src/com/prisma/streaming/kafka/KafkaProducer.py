'''
Created on Sep 6, 2016

@author: rbhat
'''

""" 
    Sends Kafka message producer. Use python version of producer. Please download kafka from http://kafka.apache.org/downloads.html first and follow
    http://kafka.apache.org/documentation.html for setting up the broker/client. Also for python client for kafka please pip https://github.com/mumrah . 
    ie. pip install python-kafka
    
"""

import time
import pandas as pd
#from kafka import KafkaConsumer, KafkaProducer

from kafka import SimpleProducer, KafkaClient
from kafka.common import LeaderNotAvailableError


def print_response(response=None):
    if response:
        print('Error: {0}'.format(response[0].error))
        print('Offset: {0}'.format(response[0].offset))


def Producer(msg):
    #producer = KafkaProducer(bootstrap_servers='deepc04.acis.ufl.edu:9092')
    #producer.send('test', b"testingt123456")
    
    kafka = KafkaClient("deepc06.acis.ufl.edu:9092")
    producer = SimpleProducer(kafka)

    topic = b'test'
    #msg = b'Hello World from Me/Rajendra!'

    try:
        print_response(producer.send_messages(topic, msg))
    except LeaderNotAvailableError:
        # https://github.com/mumrah/kafka-python/issues/249
        time.sleep(1)
        print_response(producer.send_messages(topic, msg))

    kafka.close()


df = pd.read_csv("/home/rajendra/workspace/Prisma/data/processed_data.csv")
#df = pd.read_csv("/home/rajendra/workspace/csv/processed_data.csv")
#df_json = df.to_json(orient="records")#df.reset_index().to_json()
df =  df.iloc[:1,:]
print df.columns
print df.dtypes

#print pd.__version__


for idx, row in df.iterrows():
    df_json = row.to_json() #df.reset_index().to_json(orient="records")
    msg = df_json
    print msg
    Producer(msg)

    
#for msg in messages:
#    msg_str = json.dumps(msg)
#    print(msg_str)
    
#Producer()
    
