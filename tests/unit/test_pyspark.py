from dbapp.testlib import to_list

def test_spark(spark):
    """Test if spark fixture is initialized properly"""
    df = spark.range(1)
    actual = [r.asDict() for r in df.collect()]
    expect = [dict(id=0)]
    assert actual == expect
