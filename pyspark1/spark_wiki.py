# from spark wikipedia create 5 text files of
#     Spark Core
#      Spark SQL
#      Spark Streaming
#      MLlib Machine Learning Library
#      GraphX
#find word count of each text file
#find common words in each text file and convert to list
#find 5 repeating words-convert to list
# distinct words -convert to list
#from each 5 text file top 10 repeating word
#from all text file top 10 repeating word
#make these words to a single line/one value (reduce 'x'+','+'y')

# translate({ord('.'):None,ord('['):' ',ord(']'):' ',ord(','):None,ord('-'):' ',ord(':'):' ',ord('('):None,ord(')'):None})
# rdd_gs=rdd_graph.flatMap(lambda x:x.replace('.',None).replace('[',None).replce(']',None).replace(']',None).replace(',',None).replce(.split())

#word count of each text file
import re
from pyspark import SparkContext
sc=SparkContext('local','createrdd')
rdd_graph=sc.textFile('/home/user/pythondoc/graphx')
rdd_gs=rdd_graph.flatMap(lambda x:x.translate({ord('.'):None,ord('['):' ',ord(']'):' ',ord(','):None,ord('-'):' ',ord(':'):' ',ord('('):None,ord(')'):None}).split())
# rdd_gfil=rdd_gsplit.filter(lambda x:(str.isalpha(x)))
rdd_gfil=rdd_gs.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_gmap=rdd_gfil.map(lambda x:(x.lower(),1))
rdd_gred=rdd_gmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_gred.foreach(print)
print('-'*40)
list_g=rdd_gred.map(lambda x:x[1]).collect()
print(sum(list_g))
print('-'*40)
print('-'*40)

rdd_core=sc.textFile('/home/user/pythondoc/spark_core')
rdd_csplit=rdd_core.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_cfil=rdd_csplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_cmap=rdd_cfil.map(lambda x:(x.lower(),1))
rdd_cred=rdd_cmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_cred.foreach(print)
print('-'*40)
list_c=rdd_cred.map(lambda x:x[1]).collect()
print(sum(list_c))
print('-'*40)
print('-'*40)

rdd_mlib=sc.textFile('/home/user/pythondoc/mlib')
rdd_msplit=rdd_mlib.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_mfil=rdd_msplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_mmap=rdd_mfil.map(lambda x:(x.lower(),1))
rdd_mred=rdd_mmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_mred.foreach(print)
print('-'*40)
list_m=rdd_mred.map(lambda x:x[1]).collect()
print(sum(list_m))
print('-'*40)
print('-'*40)

rdd_sql=sc.textFile('/home/user/pythondoc/spark_sql')
rdd_sqsplit=rdd_sql.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_sqfil=rdd_sqsplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_sqmap=rdd_sqfil.map(lambda x:(x.lower(),1))
rdd_sqred=rdd_sqmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_sqred.foreach(print)
print('-'*40)
list_sq=rdd_sqred.map(lambda x:x[1]).collect()
print(sum(list_sq))
print('-'*40)
print('-'*40)

rdd_st=sc.textFile('/home/user/pythondoc/spark_stream')
rdd_stsplit=rdd_st.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_stfil=rdd_stsplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_stmap=rdd_stfil.map(lambda x:(x.lower(),1))
rdd_stred=rdd_stmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_stred.foreach(print)
print('-'*40)
list_st=rdd_stred.map(lambda x:x[1]).collect()
print(sum(list_st))
print('-'*40)
rdd_stfil.distinct()
print('-'*40)
##common
rdd_comn=rdd_gfil.intersection(rdd_cfil).intersection(rdd_mfil).intersection(rdd_sqfil).intersection(rdd_stfil)
lst_comn=rdd_comn.collect()
print(lst_comn)
print('-'*40)
#distinct word from each text file
lst_graph=rdd_gred.map(lambda x:x[0]).collect()
print(lst_graph)
print('-'*50)
lst_core=rdd_cred.map(lambda x:x[0]).collect()
print(lst_core)
print('-'*50)
lst_mlib=rdd_mred.map(lambda x:x[0]).collect()
print(lst_mlib)
print('-'*50)
lst_sql=rdd_sqred.map(lambda x:x[0]).collect()
print(lst_sql)
print('-'*50)
lst_stream=rdd_stred.map(lambda x:x[0]).collect()
print(lst_stream)
print('-'*50)

#top 10 repeating from each
print('top 10 repeating word from each txt file')
gr_10=rdd_gred.map(lambda x:x[0]).take(10)
print(gr_10)
print('-'*50)
core_10=rdd_cred.map(lambda x:x[0]).take(10)
print(core_10)
print('-'*50)
mlib_10=rdd_mred.map(lambda x:x[0]).take(10)
print(mlib_10)
print('-'*50)
sql_10=rdd_sqred.map(lambda x:x[0]).take(10)
print(sql_10)
print('-'*50)
stream_10=rdd_stred.map(lambda x:x[0]).take(10)
print(stream_10)
print('-'*50)

#from all text file most 10 repeating word

rdd_join=rdd_gred.union(rdd_cred).union(rdd_mred).union(rdd_sqred).union(rdd_stred)
rdd_j_red=rdd_join.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
lst_10=rdd_j_red.map(lambda x:x[0]).take(10)
print(lst_10)
# in single line
# lst_10=rdd_j_red.map(lambda x:x[0])
# s1=rdd3.reduce(lambda x,y:str(x)+"-"+str(y))
rdd4=sc.parallelize(lst_10)
lst=rdd4.reduce(lambda x,y:str(x)+","+str(y))
print(lst)
# lst_11=rdd_j_red.map(lambda x:x[0]).reduce(lambda x,y:str(x)+","+str(y))[0:33]
# print(','.join(lst_10))
print(lst_11)

#most repeating from each text file

mr=rdd_gred.first() #action
print("max no of repeats I st txt =" ,mr[0])
mr1=rdd_cred.first() #action
print("max no of ",mr1[0])
mr2=rdd_mred.first() #action
print(mr2[0])
mr3=rdd_sqred.first() #action
print(mr3[0])
mr4=rdd_stred.first() #action
print(mr4[0])
#of ,is,on etc are stop words 




sc.stop()


#
# 5 text file save find each text file word count,find common words in 5 and convert to list,distinct words list,from each 5 top 10 repeating word
# from all 5 top 10 repeating words
# make the tope 10 words to one value a line reduce 'x'+','+'y'