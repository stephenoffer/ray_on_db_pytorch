from pyspark.sql import SparkSession

def get_dbutils(spark):
    try:
        from pyspark.dbutils import DBUtils
        dbutils = DBUtils(spark)
    except ImportError:
        import IPython
        dbutils = IPython.get_ipython().user_ns["dbutils"]
    return dbutils


def file_exists(path):
    spark = SparkSession.builder.getOrCreate()
    dbutils = get_dbutils(spark)
    try:
        dbutils.fs.ls(path)
        return True
    except Exception:
        return False
