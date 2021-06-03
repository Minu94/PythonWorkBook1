from pyspark import SparkContext
sc=SparkContext('local','createrdd')
# join,can join only  key value pair

rdd1=sc.range(13,100)
rdd2=sc.range(101,200)
# here rdd1,rdd2 is not a pair rdd,if its a pair rdd no need to add key,index is used as key
#adding key and making index
#index will be added on right so it will be moved to left ,to make key value pair key is on left, using lambda

rdd1=rdd1.zipWithIndex().map(lambda x:(x[1],x[0]))
rdd2=rdd2.zipWithIndex().map(lambda x:(x[1],x[0]))

rdd1.join(rdd2).foreach(print)
print('-'*40)

# in transformation:- convert one rdd to another rdd ,transformation-does not run
#in action:-convert rdd to list ,map etc(actins:count ,foreach,collect etc)
# transformation runs only when we call action (lazy evaluation)
# transformations run altogether not one by one (like map reduce)
#its create a graph till we call for action -lineage

##ACTIONS
#collect -convert full rdd to a list
# rdd3=sc.range(1,10)  #transformation
# print(rdd3.collect())  #action

#count-no of values or lines

# print(rdd3.count())   #action

#take- values will be taken from the top,like sql limit,result will be list
# print(rdd3.take(3))

#first
# print(rdd3.first())

#foreach-to print

#reduce -add values,multiply value ,any operations ,used for usual rdd not for rdd pair
# s=rdd3.reduce(lambda x,y:x+y)
# s1=rdd3.reduce(lambda x,y:str(x)+"-"+str(y))
# s2=rdd3.reduce(lambda x,y:x*y)
# print(s)
# print(s1)

#countByvalue-no of occurance of each value

# rdd6=sc.parallelize(([1,1,1,2,3,2,3,2,3]))
# print(rdd6.countByValue())
# print('-'*40)

#multiplication of nos from 1 to 10

# rdd_m=sc.range(1,10)
# rdd_m_res=rdd_m.reduce(lambda x,y:x*y)
# print(rdd_m_res)

#most repeated word

# rdd_t=sc.textFile('/home/user/pythondoc/song') #transformation
# rdd_split=rdd_t.flatMap(lambda x:x.split()) #transfo
# rdd_pair=rdd_split.map(lambda x:(x,1)) #transfor
# rdd_wc=rdd_pair.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False) #transfo
# mr=rdd_wc.first() #action
# print(mr[0])

#most repeated  10 word

# mr1=rdd_wc.map(lambda x:x[0]).take(10)
# print(mr1)



sc.stop()