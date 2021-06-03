from pyspark import SparkContext
sc=SparkContext('local','createrdd')
rdd1=sc.textFile('/home/user/pythondoc/song')
# rdd_split=rdd1.flatMap(lambda x:x.replace(","," ").split()) only one replcaed
# rdd_split=rdd1.flatMap(lambda x:x.strip("?.'").split()) #not worked remove combination from left ,right
rdd_split=rdd1.flatMap(lambda x:x.translate({ord('?'):None,ord(','):None,ord('.'):None}).split()) #ord to get unicode
rdd_pair=rdd_split.map(lambda x:(x,1))
rdd_wc=rdd_pair.reduceByKey(lambda x,y:x+y)
rdd_wc.foreach(print)
print('_'*40)
rdd_wc=rdd_pair.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
#most repeated word
mr=rdd_wc.first()
print(mr[0])
#most repeated 10 word
mr1=rdd_wc.map(lambda x:x[0]).take(2)
print(mr1)
sc.stop()


# 5 text file save find each text file word count,find common words in 5 and convert to list,distinct words list,from each 5 top 10 repeating word
# from all 5 top 10 repeating words
# make the tope 10 words to one value a line reduce 'x'+','+'y'