from pyspark import SparkContext
sc=SparkContext('local','createrdd')
##list comprehension continue

c='human'
x=[x for x in c ]
print(x)

alp=[chr(i) for i in range (97,123)]
print(alp)

 ##filter-only filter particular numbers that satisfy certain conditions

 #rdd for printing even nos

rddf=sc.parallelize([1,2,3,4,5,6,7,8])
rddf1=rddf.filter(lambda x:x%2==0)
rddf1.foreach(print)
print('_'*40)

#rdd for printing no.s divisible by 8 between 50 to 500
rddf2=sc.range(50,501)
rddf3=rddf2.filter(lambda x:x%8==0)
rddf3.foreach(print)
print('_'*40)

##union(element may occur repeatedly),intersection,distinct

rddu1=sc.range(2,10)
rddu2=sc.range(5,15)
rddi=rddu1.intersection(rddu2)
rddu=rddu1.union(rddu2)
rddu.foreach(print)
print('_'*100)
rddi.foreach(print)
print('_'*100)
rdd3=sc.parallelize([1,2,3,4,5,6,7,8,3,4,5,2,4,90,78,67,5])
rdd4=rdd3.distinct()
rdd4.foreach(print)
##operations for key value pair form in rdd
##group by key
rdd_text=sc.parallelize(['I am Happy','I am sad','I am angry'])
rdd_word=rdd_text.flatMap(lambda x:x.split())
rdd_pair=rdd_word.map(lambda x:(x,1))
rdd_pair.foreach(print)
print('_'*40)
rdd_gbk=rdd_pair.groupByKey()
rdd_gbk.foreach(print) #we get key and a iterable object (we can iterate using for loop)
rdd_gbk2=rdd_gbk.map(lambda x:(x[0],[x for x in x[1]]))
rdd_gbk2.foreach(print)
print('_'*100)
wc=rdd_gbk2.map(lambda x:(x[0],sum(x[1])))
wc.foreach(print)






















sc.stop()
