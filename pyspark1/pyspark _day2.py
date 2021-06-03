from pyspark import SparkContext
#first create sparkcontext
sc=SparkContext('local','createRDD')
#creating RDD by array
rdd1=sc.parallelize(['a','b','c'])
print(rdd1)
rdd1.foreach(print)


sc.stop()