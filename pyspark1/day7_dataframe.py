from pyspark.sql import SparkSession
spark=SparkSession.Builder().master('local').appName('diff').getOrCreate()
sc=spark.sparkContext#sparcontext also in sparksession



# dataframe: comes under spark sql df functions are in pysparsql,its a rdd with schema
##feauters
# lazy evaluation
# immutable
# fast
#faster than pandas


df=spark.createDataFrame([(1,'a'),(2,'b')],schema=('id','name'))
df.show()
print('-'*40)
#another way

df2=spark.read.csv('data')
df2.show()
print(df2.dtypes) #if inferschema not given dtypes will be string
print('-'*40)
df1=spark.read.csv('data',header=True,inferSchema=True) #dtypes will be int
print(df1.dtypes)
df1.show()

#converting df to rdd
rdd=df1.rdd
rdd.foreach(print)

sc.stop()