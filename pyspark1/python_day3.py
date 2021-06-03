
from pyspark import SparkContext
sc=SparkContext('local','createrdd')
# we can pass a list to create rdd
# ls=[5,6,7,8]
# rdd1=sc.parallelize(ls)
# rdd1.foreach(print)
# print('_'*40)  #to print below
# rdd from text file#
# rdd3=sc.textFile('/home/user/Desktop/pyspark1')
# rdd3.foreach(print)
# print('_'*40)

# rdd4=sc.range(1,101)
# rdd4.foreach(print)
# print('_'*40)
#map#
# rdd5=sc.range(5,20)
# rdd6=rdd5.map(lambda x:x*x)
# rdd6.foreach(print)
# print('_'*40)
# rdd6=rdd5.map(lambda x:[x*x,x*3]) #give list
# rdd9=rdd6.flatmap(lambda x:x)
# rdd9.foreach(print)

#two split a line by word by word


# using list
# ls2=[1,2,3,4]
# rdd7=sc.parallelize(ls2)
# rdd8=rdd7.map(lambda x:x*x)
# rdd8.foreach(print)

# Using flat map for text file
# rdd_text=sc.parallelize(['I am Happy','I am sad','I am angry']) for this split ()
# rdd_text=sc.textFile('/home/user/Downloads/sampless/custom.txt')
# rdd_text.foreach(print)
# rdd_text1=rdd_text.map(lambda x:x.split(','))
# rdd_text1.foreach(print)
# rdd_text.flatMap(lambda x:x.split(',')).map(lambda x:(x,1)).foreach(print)

# two type operations inrdd
# transformation :filter,map etc its doesnot run but  create lineage(a graph of what to do) ,its run only when we call action


#list comprehension#
# a=[i for i in range(1,10)] #give 1 2 3 4 .....10
# print(a)
# b=[i*2 for i in range(1,10)]
# print(b)
# c=['k' for i in range(1,10)]  #10 times print k
# print(c)
# d=[i*i for i in range(1,11)]
# b=[]
# for i in range(10):
    # if i%2==0:
        # b.append((i,'even'))
    # else:
        # b.append((i,'odd'))
# another way
# lc=['even' if i%2==0 else 'odd' for i in range(0,10)]

# ls=sc.range(1,10)
# js=[i**2 if i%2==0 else i**3 for i in range(10,100)]
# print(js)
# lc=[i*i for in range(0,10) if i%2==0] for if only used it used at end
# l3=[i/5 for i in range (5,20) if i%5==0]
# print(l3)
# l3 = [i / 5 for i in range(5, 20) if i % 5 == 0 if i%2==0] check for nos divide by both 2 and 5
l2=['small' if i<25 else 'medium' if i<70 else 'large' for i in range (1,101)]
print(l2)
sc.stop()