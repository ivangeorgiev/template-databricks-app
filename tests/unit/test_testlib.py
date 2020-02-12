"""Tests for the testlib module"""

import pytest
import pyspark.sql.types as pst
from dbapp.testlib import to_list

def test_as_list_deep(spark):
  """as_list converts rows to dictionary deeply"""
  input = [ pst.Row(id=1, a=pst.Row(b=101)) ]
  input_df = spark.createDataFrame(input)

  actual = to_list(input_df, True)
  expect = [{'id':1, 'a':{'b':101}}]

  assert actual == expect

def test_as_list_shallow(spark):
  """as_list converts rows to dictionary without deep"""
  input = [ pst.Row(id=1, a=pst.Row(b=101)) ]
  input_df = spark.createDataFrame(input)

  actual = to_list(input_df, False)
  expect = [{'id':1, 'a':pst.Row(b=101)}]

  assert actual == expect
