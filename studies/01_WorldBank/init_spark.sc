import $exclude.`org.slf4j:slf4j-log4j12`, $ivy.`org.slf4j:slf4j-nop:1.7.21` // for cleaner logs
import $profile.`hadoop-2.6`
import $ivy.`org.apache.spark::spark-sql:2.1.0` // adjust spark version - spark >= 2.0
import $ivy.`org.apache.hadoop:hadoop-aws:2.6.4`
import $ivy.`org.jupyter-scala::spark:0.4.2` // for JupyterSparkSession (SparkSession aware of the jupyter-scala kernel)

import org.apache.spark._
import org.apache.spark.sql._
import jupyter.spark.session._

val sparkSession = JupyterSparkSession.builder() // important - call this rather than SparkSession.builder()
  .jupyter() // this method must be called straightaway after builder()
  // .yarn("/etc/hadoop/conf") // optional, for Spark on YARN - argument is the Hadoop conf directory
  // .emr("2.6.4") // on AWS ElasticMapReduce, this adds aws-related to the spark jar list
  .master("local") // change to "yarn-client" on YARN
  // .config("spark.executor.instances", "10")
  // .config("spark.executor.memory", "3g")
  // .config("spark.hadoop.fs.s3a.access.key", awsCredentials._1)
  // .config("spark.hadoop.fs.s3a.secret.key", awsCredentials._2)
  .appName("notebook")
  .getOrCreate()
