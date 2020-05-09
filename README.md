# mlflow-project-example

NOTE: This code needs to be updated for Spark 3.0!

To run this code locally, you can clone the repo and execute:
* mlflow run . -P file_path=data/sf-airbnb-clean.parquet -P max_depth=5 -P num_trees=100

Or, you can run it this way:
* mlflow.run("https://github.com/brookewenig/mlflow-project-example", parameters={"max_depth": 5, "num_trees": 100})

To run the code from Databricks:
* mlflow run https://github.com/brookewenig/mlflow-project-example -P max_depth=5 -P num_trees=100  
* mlflow.run("https://github.com/brookewenig/mlflow-project-example", parameters={"max_depth": 5, "num_trees": 100})