
1. Install Kafka in Ubuntu Server

pip install kafka-python

2. Setting up pyspark with eclipse
#https://enahwe.wordpress.com/2015/11/25/how-to-configure-eclipse-for-developing-with-python-and-spark-on-hadoop/
#https://javadeveloperblog.wordpress.com/eclipse-related/pyspark-use-case-project-setup-eclipse-pydev/

>PyDev -> “Interpreter – Python”
>Click “New”
>Browse “Python.exe” from Python installation folder
>click “Ok”

>Select “Libraries” tab
>Click “New Folder”
>chose the following folders
><spark_home>/python
><spark_home>/python/pyspark
>Click “New Egg/Zip(s)”
>chose the following folders
><spark_home>/python/lib/py4j-0.8.2.1-src.zip
><spark_home>/python/lib/pyspark.zip
>Select “Environment” tab
>Click “New”
>Enter “SPARK_HOME” and browse the “spark home folder (<spark_home>)”
>Click “Ok”

>Click on “Apply”
>Click on “Ok”
>File -> New -> Other
>Chose “PyDev Project” from the New Dialog box (or wizard)
>click “Next”
>Enter project Name
>select radio button “create src folder and add it to the PYTHONPATH?”
>Click “Finish”

3. nltk
sudo pip install -U nltk
sudo apt-get install nltk-python
>import nltk
>nltk.download("stopwords")

3. Install rpy2
sudo pip install rpy2

4. Install schedule
sudo pip install schedule

5. cassandra
sudo pip install cassandra-driver

http://rustyrazorblade.com/2015/05/on-the-bleeding-edge-pyspark-dataframes-and-cassandra/

6. http://blog.katychuang.com/blog/2015-09-30-kafka_spark.html

7. 
spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.5.0,TargetHolding/pyspark-cassandra:0.1.5 
   --conf spark.cassandra.connection.host=deepc04.acis.ufl.edu Cassandra.py my-topic

8. 
spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.5.0,TargetHolding/pyspark-cassandra:0.1.5 
   --conf spark.cassandra.connection.host=deepc04.acis.ufl.edu IrisDemo.py









