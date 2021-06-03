import collections
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
sc=SparkContext("local","wordcount")

sql=SQLContext(sc)
var1=sc.broadcast(open("/home/user/Downloads/pysparksqlexamples/book.txt","r+").readlines())
num=sc.accumulator(0)
# list2=sc.accumulator([])
list2=[]
from functools import reduce
def wordcount(i):
    global var1
    global num
    global list2
    num+=i
    # c=num.value
    sentences=var1.value
# print(sentences)
    words=reduce(lambda a,b:a+b if a!=None else [] ,map(lambda s:s.split(" "),filter(lambda s:s!='' ,sentences)))
    allwords=words
    uniqueword= set(allwords)
    wordcount={w:allwords.count(w) for w in uniqueword}
    # sorted_x = sorted(x.items(), key=lambda kv: kv[1])
    # sorted_dict = collections.OrderedDict(sorted_x)
    # list2=[]
    for count in wordcount.items():
       list2.append(count)
    return list2
    # print(list2)




# df = sql.createDataFrame(list2)
    # sc.broadcast(list2)
    # rdd1=sc.parallelize(list2)
    df = sql.createDataFrame(list2)
    df.show()



# print(list2)
rdd=sc.parallelize([1,2])
rdd2=rdd.foreach(lambda i:wordcount(i))
# rdd2.foreach(print)





sc.stop()