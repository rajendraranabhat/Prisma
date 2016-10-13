'''
Created on Sep 6, 2016

@author: rbhat
'''
"""
Kafka Spark Streaming Consumer    
"""

import sys
import os
import json
import re
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
from pyspark.sql import SQLContext
from pyspark.sql import Row
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD, LogisticRegressionWithLBFGS

from IrisStream import *
from predict_gam import *
from SchemaTable import *
#from com.prisma.streaming.util import Utility

#sys.path.append("~/workspace/Prisma")

#import pyspark_cassandra
#from pyspark_cassandra import streaming

def read_csv():
    """
    df = sqlContext.read.format('com.databricks.spark.csv').\
         options(header='true', inferschema='true').\
         load('/home/rajendra/workspace/Prisma/data/processed_data.csv')    
    df.registerTempTable("Prisma")"""

def process(rdd):
    
    if rdd.isEmpty():
        return
    
    df = sqlContext.createDataFrame(rdd,schema_data)  
       
    #df = sqlContext.createDataFrame(rdd, samplingRatio=0.4) #samplingRatio for infering schema  
    #df.show()
    #df.select(df['acc'],df['age'],df['Gender']).show()
    #df.printSchema()
    
    df_pand = df.toPandas()    
    #print df_pand
        
    pred = predict(df_pand)
    #pred.columns = map(str.lower, pred.columns)        
    
    pred = pred[['acc','score_cvcomp','score_mvcomp','score_icucomp','score_woundcomp',\
                 'score_neuro_delirium','score_sepsis','score_vte','score_aki']]
    
    #print 'pred: ', pred
    
    df_mf = sqlContext.createDataFrame(pred)
    
    predict_table = sqlContext.read.format("org.apache.spark.sql.cassandra").load(keyspace="prisma", table="predict")
    
    df_mf.select(df_mf['acc'],df_mf['score_cvcomp'],df_mf['score_mvcomp']).write.format("org.apache.spark.sql.cassandra").\
          options(table="predict", keyspace="prisma").save(mode="append")


if __name__ == "__main__":
    
    #if len(sys.argv) != 3:
    #    print("Usage: kafka_spark_consumer_01.py <zk> <topic>", file=sys.stderr)
    #    exit(-1)
    
    #Settong up the environment to run locally.
    #Utility.setEnvironment()
    
    conf = SparkConf().setAppName("PrismaPStreaming").set("spark.cassandra.connection.host", "deepc04.acis.ufl.edu")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    ssc = StreamingContext(sc, 1)
    
    #zkQuorum, topic = sys.argv[1:]
    
    zkQuorum = "deepc06.acis.ufl.edu:2181"
    topic    = "test"
 
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "PrismaPStreamingKafka", {topic: 1})
    dstream = kvs.map(lambda x: json.loads(x[1]))    
   
    dstream.foreachRDD(process)
            
    #dstream.pprint()
    #print(type(dstream))
    #dstream.saveAsTextFiles('pris.json') 
       
    ssc.start()
    ssc.awaitTermination()

    
    