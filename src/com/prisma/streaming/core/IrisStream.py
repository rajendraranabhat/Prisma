'''
Created on Oct 9, 2016

@author: rajendra
'''

import re
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD, LogisticRegressionWithLBFGS


NameToValue = {
    'setosa': 0,
    'versicolor': 1,
    'virginica': 2
}

def irisData(lines, sqlContext):
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
    
    
    