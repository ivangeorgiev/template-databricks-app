"""
Helper functions for use in automated tests.
"""

import pyspark.sql
import pyspark.sql as ps
import pyspark.sql.types as pst

def to_list(input_df:pyspark.sql.DataFrame, 
            deep:bool=True):
    """
    Convert Spark DataFrame to list.

    Collects rows from Spark DataFrame and converts each row to
    a dictionary. Optionally perform deep Row to dictionary conversion.

    Parameters
    ----------
    input_df : pyspark.sql.DataFrame
        Spark DataFrame to be collected.
    deep : bool
        Specify whether the Row to dictionary conversion needs to be
        deep. Optional (default: True) 

    Returns:
    --------
    list
        List of dictionary. Contains one item of dictionary type for each
        row from the input Spark DataFrame.
    """
    def row_as_dict(r):
      d = r.asDict()
      if deep:
        for k in d:
          if isinstance(d[k], pst.Row):
            d[k] = row_as_dict(d[k])
      return d
    
    if isinstance(input_df, ps.DataFrame):
        result = [row_as_dict(r) for r in input_df.collect()]
    else:
        result = input_df
    return result
