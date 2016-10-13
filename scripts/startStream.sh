#!/bin/bash

#Make sure you can execute python file. chmod +x 

export PYTHONPATH='${PYTHONPATH}:$HOME/workspace/Prisma'

spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.5.0,TargetHolding:pyspark-cassandra:0.3.2,com.databricks:spark-csv_2.11:1.3.0 ../src/com/prisma/streaming/core/SparkStreaming.py

