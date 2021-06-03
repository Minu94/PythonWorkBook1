from pyspark import SparkContext
sc=SparkContext('local','createrdd')
rdd1=sc.textFile('/home/user/pythondoc/song')
rdd_word=rdd1.flatMap(lambda x:x.split())
rdd_pair=rdd_word.map(lambda x:(x,1))
rdd_gbk=rdd_pair.groupByKey()
rdd_gbk2=rdd_gbk.map(lambda x:(x[0],[x for x in x[1]]))
wc=rdd_gbk2.map(lambda x:(x[0],sum(x[1])))

wc.foreach(print)

sc.stop()
#most repeating word