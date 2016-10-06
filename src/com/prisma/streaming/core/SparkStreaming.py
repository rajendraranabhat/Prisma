'''
Created on Sep 6, 2016

@author: rbhat
'''
from com.prisma.streaming.util import Utility

"""
Kafka Spark Streaming Consumer    
"""

import sys
import os
import json
import re
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD, LogisticRegressionWithLBFGS

from com.prisma.streaming.util.Utility import *
#import pyspark_cassandra
#from pyspark_cassandra import streaming

NameToValue = {
    'setosa': 0,
    'versicolor': 1,
    'virginica': 2
}

if __name__ == "__main__":
    
    #if len(sys.argv) != 3:
    #    print("Usage: kafka_spark_consumer_01.py <zk> <topic>", file=sys.stderr)
    #    exit(-1)
    
    #Settong up the environment to run locally.
    #Utility.setEnvironment()
    
    sc = SparkContext(appName="PrismaPStreaming")
    sqlContext = SQLContext(sc)
    ssc = StreamingContext(sc, 1)
    
    #zkQuorum, topic = sys.argv[1:]
    
    zkQuorum = "deepc04.acis.ufl.edu:2181"
    topic    = "test"
    
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "PrismaPStreamingKafka", {topic: 1})
    lines = kvs.map(lambda x: x[1])
    #counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
    #counts.pprint()
    
    
    #data_raw = sc.textFile(inputFile)
    multiline_iris_rdd = lines #sc.wholeTextFiles(inputFile)
    iris_rdd = multiline_iris_rdd.map(lambda x : x[1]).map(lambda x : re.sub(r"\s+", "", x, flags=re.UNICODE))
    iris_df1=sqlContext.jsonRDD(iris_rdd)
    iris_df1.printSchema()
    iris_df1.show(4)
    
    iris_df1 = iris_df1.map(lambda l: LabeledPoint(NameToValue[l[-1]],l[:-1]))

    trainIris, testIris = iris_df1.randomSplit([0.7, 0.3])
    model = LogisticRegressionWithLBFGS.train( trainIris , numClasses=3) #For Multinomial classification
    prediction_and_labels = testIris.map(lambda point: (model.predict(point.features), point.label))
    correct = prediction_and_labels.filter(lambda (predicted, actual): predicted == actual)
    accuracy = correct.count() / float(testIris.count())
    
    print "Classifier correctly predicted category " + str(accuracy * 100) + " percent of the time"
    
    
    ssc.start()
    ssc.awaitTermination()
    
        
    