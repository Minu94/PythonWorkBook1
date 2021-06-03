from pyspark import SparkContext
sc=SparkContext('local','createrdd')
# rdd1=sc.range(5,50)
# lst1=rdd1.filter(lambda x:x%5==0)
# lst1.foreach(print)
# print('_'*40)
# rdd2=sc.range(15,60)
# lst2=rdd2.union(rdd1)
# lst2.foreach(print)
# print('-'*40)
# lst4=rdd2.intersection(rdd1)
# lst4.foreach(print)
# print('-'*40)
# lst3=rdd2.distinct()
# lst3.foreach(print)
# print('-'*40)

#word count,python wikipedia
rdd_txt=sc.textFile('/home/user/pythondoc/pythonly')
rdd_w=rdd_txt.flatMap(lambda x:x.split())
rdd_p=rdd_w.map(lambda x:(x.lower(),1))
rdd_gbk=rdd_p.groupByKey()
rdd_gbk2=rdd_gbk.map(lambda x:(x[0],[x for x in x[1]]))
wc=rdd_gbk2.map(lambda x:(x[0],sum(x[1])))
wc.foreach(print)
print('-'*40)
# another way
rdd_wc_gbk=rdd_txt.flatMap(lambda x:x.split()).map(lambda x:(x.lower(),1)).groupByKey().map(lambda x:(x[0],sum(x[1])))
rdd_wc_gbk.foreach(print)
print('-'*40)
#another way,using reduceByKey (1,1),(1,2),(2,3),(1,4) first cosider key 1 and check for similar keys 1
#(1,1)1,y=1 result(1,1)
#next(1,2) x=1 y=2 result(
rdd_wc=rdd_p.reduceByKey(lambda x,y:x+y)
rdd_wc.foreach(print)

#to get in alphabetical order
rdd_wc_sort=rdd_wc_gbk.sortByKey()
rdd_wc_sort.foreach(print)
print('-'*40)
#sorting values in descending order
rdd_wc_sort2=rdd_wc_gbk.map(lambda x:(x[1],x[0])).sortByKey(ascending=False)
rdd_wc_sort2.foreach(print)
print('-'*40)
#using sortBY
rdd_wc_srt=rdd_wc_gbk.sortBy(lambda x:x[1],ascending=False)
rdd_wc_srt.foreach(print)
print('-'*40)

#map split and give list
#each word line by line flat map
sc.stop()