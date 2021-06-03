from pyspark.sql import SparkSession
spark = SparkSession.Builder().master('local').appName('anb').getOrCreate()
sc = spark.sparkContext

df=spark.read.csv('/home/user/Downloads/data.csv',header=True,inferSchema=True)
df.show()
#since first column has no name it automatically give the name c0
#operations
##print schema-columns and data types
df.printSchema()
##select -to select columns
df1=df.select('Name')
df1.show()
df2=df.select('Name','Age') #multiple columns
df2.show()
df3=df.select('_c0', 'ID', 'Name', 'Age', 'Nationality','Overall', 'Potential', 'Club', 'Value', 'Wage','Preferred Foot','Joined','Contract Valid Until')

print(df3.first()) #first row
print(df3.head()) #similar to first()
print(df3.head(1)) #list of first row
##count-no of rows
print(df3.count)
##columns
print(df3.columns) #list of columns
print(len(df3.columns)) #no of columns
##to get name in first row
print(df3.first()['Name'])
##describe-similar to describe in pd

df3.describe().show()
##distict

df3.select('age').distinct().show()
df3.select('Nationality').distinct().show() #does not change orginal

##filter

dff=df3.filter(df3['Nationality']=='Russia') #not case sensitive NAtionality #1
dff1=df3.filter(df3.Nationality=='Russia') #same as above,case sensitive #2
from pyspark.sql.functions import col
ff=df3.filter(col('Nationality')=='Argentina') #easy way #3
ff3=df3.filter(col('Preferred Foot')=='Left')

ff3.show()
dff.show()
dff1.show()
##groupBy
df3.groupBy('Nationality').count().show()
#to order
df3.groupBy('Nationality').count().orderBy('count',ascending=False).show()
##to find null value in a column
dff_n=df3.filter(col('Joined').isNull())
print(dff_n)
print(dff_n.count())
ff2=df3.filter((col('Nationality')=='Argentina') &( col('Age')<30))
ff2.show()




sc.stop()