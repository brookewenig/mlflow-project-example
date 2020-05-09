from pyspark.sql import SparkSession
import mlflow
import pandas as pd
import click

spark = SparkSession.builder.appName("App").getOrCreate()

@click.command()
@click.option("--file_path", default="data/sf-airbnb-clean.parquet", type=str)
@click.option("--num_trees", default=20, type=int)
@click.option("--max_depth", default=5, type=int)
def mlflow_rf(file_path, num_trees, max_depth):
  with mlflow.start_run(run_name="random-forest") as run:
    # Create train/test split
    airbnbDF = spark.read.parquet(file_path)
    (trainDF, testDF) = airbnbDF.randomSplit([.8, .2], seed=42)
    
    # Log params: Num Trees and Max Depth  
    mlflow.log_param("num_trees", num_trees)
    mlflow.log_param("max_depth", max_depth)
    
    # Log metric
    mlflow.log_metric("count", trainDF.count())

if __name__ == "__main__":
  mlflow_rf()