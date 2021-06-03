import re
from pyspark import SparkContext
sc=SparkContext('local','createrdd')#local run on local,not in cloud,createrdd app name
ls1=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there',
'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own',
'an', 'be’, ‘some’, ‘for', 'do','its', 'yours' , 'such', 'into', 'of', 'most',
'itself', 'other’, ‘off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each',
'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
'don', 'nor', 'me', 'were','her', 'more', 'himself', 'this', 'down', 'should', 'our',
'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when',
'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
'yourselves', 'then']
ls=['a','the','an','is','was','as','on','of']
rdd1=sc.parallelize(ls)
rdd_graph=sc.textFile('/home/user/pythondoc/graphx')
rdd_gs=rdd_graph.flatMap(lambda x:x.translate({ord('.'):None,ord('['):' ',ord(']'):' ',ord(','):None,ord('-'):' ',ord(':'):' ',ord('('):None,ord(')'):None}).split())
# rdd_gfil=rdd_gsplit.filter(lambda x:(str.isalpha(x)))
rdd_gfil=rdd_gs.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_gmap=rdd_gfil.map(lambda x:(x.lower(),1))
rdd_gred=rdd_gmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)



rdd_core=sc.textFile('/home/user/pythondoc/spark_core')
rdd_csplit=rdd_core.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_cfil=rdd_csplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_cmap=rdd_cfil.map(lambda x:(x.lower(),1))
rdd_cred=rdd_cmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)



rdd_mlib=sc.textFile('/home/user/pythondoc/mlib')
rdd_msplit=rdd_mlib.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_mfil=rdd_msplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_mmap=rdd_mfil.map(lambda x:(x.lower(),1))
rdd_mred=rdd_mmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_mred.foreach(print)
print('-'*40)

rdd_sql=sc.textFile('/home/user/pythondoc/spark_sql')
rdd_sqsplit=rdd_sql.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_sqfil=rdd_sqsplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_sqmap=rdd_sqfil.map(lambda x:(x.lower(),1))
rdd_sqred=rdd_sqmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_sqred.foreach(print)
print('-'*40)


rdd_st=sc.textFile('/home/user/pythondoc/spark_stream')
rdd_stsplit=rdd_st.flatMap(lambda x:x.translate({ord('.'):' ',ord('"'):' ',ord("/"):' ',ord('['):' ',ord(']'):' ',ord(','):' ',ord('-'):' ',ord(':'):' ',ord('('):' ',ord(')'):' '}).split())
rdd_stfil=rdd_stsplit.filter(lambda x:re.sub(r"[0-9]",'',x))
rdd_stmap=rdd_stfil.map(lambda x:(x.lower(),1))
rdd_stred=rdd_stmap.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd_stred.foreach(print)
print('<<'*40)
rdd_comn=rdd_gfil.intersection(rdd_cfil).intersection(rdd_mfil).intersection(rdd_sqfil).intersection(rdd_stfil)

rdd10=rdd_comn.filter(lambda x:x not in ls1 )
rdd10.foreach(print)


sc.stop()


