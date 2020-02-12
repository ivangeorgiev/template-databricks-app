import pytest

@pytest.fixture(scope="session", name="spark", autouse=True)
def get_spark():
    global spark

    if not 'spark' in globals():
        import os
        from pyspark.sql import SparkSession
        os.environ['SPARK_LOCAL_IP'] = "127.0.0.1"
        spark = SparkSession.builder.getOrCreate()
        logger = spark.sparkContext._jvm.org.apache.log4j
        logger.LogManager.getRootLogger().setLevel(logger.Level.ERROR)
    yield spark

