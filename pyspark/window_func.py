from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number, rank, dense_rank, sum, lag
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("WindowFunctionsExample").getOrCreate()

# Sample Data
data = [
    ('Alice', 'Sales', 1000),
    ('Bob', 'Sales', 1500),
    ('Charlie', 'HR', 2000),
    ('David', 'HR', 2200),
    ('Eve', 'IT', 3000),
    ('Frank', 'IT', 3200)
]
columns = ['Name', 'Department', 'Salary']
df = spark.createDataFrame(data, columns)
df.show()

# +-------+----------+------+
# |   Name|Department|Salary|
# +-------+----------+------+
# |  Alice|     Sales|  1000|
# |    Bob|     Sales|  1500|
# |Charlie|        HR|  2000|
# |  David|        HR|  2200|
# |    Eve|        IT|  3000|
# |  Frank|        IT|  3200|
# +-------+----------+------+

# Window Specification
# To use window functions, you need to define a window specification that describes
# how the data should be partitioned and ordered.
windowSpec = Window.partitionBy("Department").orderBy("Salary")

# 1. Using row_number()
# The row_number() function assigns a unique sequential number to rows within a window partition.
df.withColumn("row_number", row_number().over(windowSpec)).show()
# +-------+----------+------+----------+
# |   Name|Department|Salary|row_number|
# +-------+----------+------+----------+
# |Charlie|        HR|  2000|         1|
# |  David|        HR|  2200|         2|
# |    Eve|        IT|  3000|         1|
# |  Frank|        IT|  3200|         2|
# |  Alice|     Sales|  1000|         1|
# |    Bob|     Sales|  1500|         2|
# +-------+----------+------+----------+

# 2. Using rank()
# The rank() function provides a ranking of rows within a window partition.
# Rows with equal values will receive the same rank, and there will be a gap in ranks after duplicates.
df.withColumn("rank", rank().over(windowSpec)).show()
# +-------+----------+------+----+
# |   Name|Department|Salary|rank|
# +-------+----------+------+----+
# |Charlie|        HR|  2000|   1|
# |  David|        HR|  2200|   2|
# |    Eve|        IT|  3000|   1|
# |  Frank|        IT|  3200|   2|
# |  Alice|     Sales|  1000|   1|
# |    Bob|     Sales|  1500|   2|
# +-------+----------+------+----+

# 3. Using dense_rank()
# The dense_rank() function is similar to rank(),
# but it does not leave gaps in the ranking sequence after duplicate values.
df.withColumn("dense_rank", dense_rank().over(windowSpec)).show()
# +-------+----------+------+----------+
# |   Name|Department|Salary|dense_rank|
# +-------+----------+------+----------+
# |Charlie|        HR|  2000|         1|
# |  David|        HR|  2200|         2|
# |    Eve|        IT|  3000|         1|
# |  Frank|        IT|  3200|         2|
# |  Alice|     Sales|  1000|         1|
# |    Bob|     Sales|  1500|         2|
# +-------+----------+------+----------+

# 4. Using Aggregation in Windows (e.g., sum())
# You can also use window functions to perform aggregations like sum(), avg(), etc., over a partition.
# For example, calculating the cumulative sum of salaries within each department:
df.withColumn("cumulative_salary", sum("Salary").over(windowSpec)).show()
# +-------+----------+------+----------------+
# |   Name|Department|Salary|cumulative_salary|
# +-------+----------+------+----------------+
# |Charlie|        HR|  2000|            2000|
# |  David|        HR|  2200|            4200|
# |    Eve|        IT|  3000|            3000|
# |  Frank|        IT|  3200|            6200|
# |  Alice|     Sales|  1000|            1000|
# |    Bob|     Sales|  1500|            2500|
# +-------+----------+------+----------------+

# 5. Using lag() and lead()
# lag(): Accesses data from the previous row within the window.
# lead(): Accesses data from the next row within the window.
# For example, using lag() to get the salary of the previous employee in the department:
df.withColumn("previous_salary", lag("Salary", 1).over(windowSpec)).show()
# +-------+----------+------+---------------+
# |   Name|Department|Salary|previous_salary|
# +-------+----------+------+---------------+
# |Charlie|        HR|  2000|           null|
# |  David|        HR|  2200|           2000|
# |    Eve|        IT|  3000|           null|
# |  Frank|        IT|  3200|           3000|
# |  Alice|     Sales|  1000|           null|
# |    Bob|     Sales|  1500|           1000|
# +-------+----------+------+---------------+
