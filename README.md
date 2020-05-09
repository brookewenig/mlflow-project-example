# mlflow-project-example

NOTE: This code needs to be updated for Spark 3.0!

To run this code locally, you can clone the repo and execute:
* mlflow run .

If you want to pass in parameters, you can specify them as well:
* mlflow run . -P file_path=data/sf-airbnb-clean.parquet -P max_depth=5 -P num_trees=100

Or, you can run it this way:
* mlflow.run("https://github.com/brookewenig/mlflow-project-example", parameters={"max_depth": 5, "num_trees": 100})