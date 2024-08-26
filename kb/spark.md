### 1. What cluster manager have you used in your project?
I have primarily used **YARN** (Yet Another Resource Negotiator) and **Kubernetes** as cluster managers. In cloud environments, I’ve also worked with **Databricks clusters** (managed on either Azure or AWS).

### 2. What is your cluster size?
The cluster size varies depending on the project, typically ranging from **10 to 50 nodes**. In cloud environments like **Azure Databricks**, the cluster is auto-scaled based on workload, starting from a few nodes and scaling up as needed.

### 3. How does your data come to your storage location?
Data arrives in **batch** or **streaming modes**:
- **Batch data** is ingested via ETL pipelines from sources like **Kafka**, **S3** (AWS), or **Azure Blob Storage**.
- **Streaming data** is fed in real-time using **Kafka**, **Azure Event Hub**, or **AWS Kinesis**.

### 4. What are the other sources you have used in your project?
Common sources include:
- **Relational databases**: PostgreSQL, MySQL
- **NoSQL databases**: MongoDB, Cassandra
- **Cloud storage**: S3, Azure Blob, Google Cloud Storage
- **Message brokers**: Kafka, EventHub
- **APIs**: REST APIs to fetch data from third-party systems.

### 5. What is the sink for your project?
Depending on the use case, sinks can include:
- **Databases**: PostgreSQL, Cassandra, S3, Azure Data Lake
- **Data warehouses**: Azure Synapse, Snowflake, Redshift
- **Data formats**: Parquet, ORC, Avro for optimized data storage.

### 6. What is the frequency of the data in your source?
Data frequency varies:
- **Batch processing**: Typically hourly or daily.
- **Streaming systems**: Real-time or near real-time (continuous).

### 7. What is the volume of your data?
The data volume ranges from **gigabytes to terabytes**. For example, in one project, we handled around **200 GB** of data per day using distributed processing tools like **Apache Spark**.

### 8. Please explain your project in detail.
In a recent project, we built a data pipeline for a public transport company. This involved ingesting data from various sources such as passenger ticketing systems, real-time GPS devices, and weather data. We used **Apache Spark** for data transformation and processing, ensuring compliance with data privacy laws by anonymizing personal information. The processed data was then made available for BI tools like **Power BI** for reporting.

### 9. 99 tasks out of 100 have completed, but the last task is taking a long time. How do you handle this?
This issue is often due to **data skew**:
- Investigate the skew by checking data distribution in partitions.
- Solutions may include salting keys to distribute data more evenly or increasing partition size.
- Alternatively, adjust Spark configurations, such as increasing executor memory for that specific task.

### 10. What challenges have you faced, and how did you overcome them?
Challenges included:
- **Data skew**: Resolved by repartitioning data and using salting techniques to even out distribution.
- **Schema evolution**: Addressed by using **Avro** with a schema registry to handle evolving data structures.

### 11. What optimization techniques have you used in your project, and why?
Key optimization techniques include:
- **Broadcast joins**: To avoid shuffling large datasets.
- **Caching intermediate results**: For iterative operations.
- **Repartitioning**: To avoid skew and optimize downstream transformations.
- **Predicate pushdown**: To filter data early and minimize I/O.

### 12. Have you done Spark optimization tuning? If yes, how?
Yes, Spark tuning involves:
- **Adjusting parallelism**: Increasing `spark.sql.shuffle.partitions` to match cluster size.
- **Memory tuning**: Setting appropriate values for `spark.executor.memory` and `spark.driver.memory`.
- **Partition pruning**: Effective partitioning for faster reads.

### 13. Can you walk me through the Spark-submit command?
```bash
spark-submit \
--class com.example.MainClass \
--master yarn \
--deploy-mode cluster \
--executor-memory 4G \
--num-executors 10 \
--executor-cores 4 \
--conf spark.sql.shuffle.partitions=200 \
example.jar
```
This example submits a Spark job to run in YARN, allocating 4 GB memory per executor, with 10 executors and 4 cores each.

### 14. 100 GB of data with 5 Actions and 3 Transformations — explain what happens.

1. **Stages and Tasks**: The data processing pipeline is divided into stages based on the transformations applied, such as `map`, `filter`, and `reduce`. Each stage is further divided into tasks based on the partitions of the data.
   
2. **Actions Trigger Computation**: Actions like `count`, `collect`, or `save` trigger the computation. These actions prompt Spark to execute the transformations and perform the necessary computations.

3. **Data Shuffling**: During execution, data may be shuffled across the network, especially during operations that require data from multiple partitions, such as joins.

4. **Execution Across the Cluster**: Spark breaks the job into multiple stages and tasks based on dependencies and executes these tasks across the cluster, leveraging distributed resources for parallel processing.

### 15. How do you take your code to a higher environment?

Code promotion through environments involves:
- **CI/CD Pipelines**: Using tools like **Jenkins** or **Azure DevOps**.
- **Development**: Initial testing in the development environment.
- **Staging**: Conducting more extensive tests in the staging environment.
- **Production**: Final deployment to the production environment after successful testing.

### 16. How do you schedule your job in production?

Jobs are scheduled using tools such as:
- **Apache Airflow**
- **Databricks Jobs**
- **AWS Step Functions**

Jobs can be set to run at specific intervals (e.g., daily or hourly) or be triggered by events.

### 17. How do you reprocess data if it fails?

Reprocessing data involves:
- **Batch Jobs**: Utilizing checkpointing or offset management to retry from the point of failure.
- **Streaming Data**: Leveraging Spark's Kafka offset management to reset offsets and reprocess the data.

### 18. One scenario where your decision went wrong and what you learned?

**Scenario**: Underestimating the impact of data skew led to performance issues and delayed task completion.
**Learning**: Analyzed data distribution early and implemented strategies like salting or repartitioning to address data skew and avoid performance bottlenecks.

### 19. How did you resolve duplicate records in a table for a particular partition?

Resolved duplicate records by:
- **Deduplication Techniques**: Applying window functions like `ROW_NUMBER()` or `RANK()` to identify and remove duplicates based on business logic.

### 20. What is the frequency of your jobs?

- **Batch Jobs**: Typically run daily or hourly.
- **Streaming Jobs**: Process data continuously in real-time or near real-time.

### 21. How do you notify your business/stakeholders in case of job failure?

Automated alerts are implemented using:
- **Email Notifications**
- **Slack Notifications**

These alerts are integrated with job orchestration tools such as **Airflow**, **Databricks**, or **Jenkins**.
