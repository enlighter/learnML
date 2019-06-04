# PySpark dataframe basics
## Link: https://www.linkedin.com/learning/spark-for-machine-learning-ai/organizing-data-in-dataframes
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
emp_df = spark.read.csv('employee.txt', header=True)

print(emp_df)
print(emp_df.schema)
# More pretty format for schema
emp_df.printSchema()
# column names of df
print(emp_df.columns)
# first 5 rows
print(emp_df.take(5))
# no. of rows
print(emp_df.count())

# Sampling:
## approximately 10% sample without replacement
sample_df = emp_df.sample(False, 0.1)
print(sample_df.count())

# e.g., say, managers are those with salary >=100,000
emp_mgrs_df = emp_df.filter("salary >=100000")
print(emp_mgrs_df.count())
emp_mgrs_df.select("salary").show()
