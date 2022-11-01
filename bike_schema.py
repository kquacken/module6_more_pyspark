from pyspark.sql.types import StructType, StructField, StringType, DateType, IntegerType

bike_schema = StructType([StructField('year',IntegerType(),True),
                          StructField('timeframe',StringType(),True),
                          StructField('week',DateType(),True),
                          StructField('counts_31_counters',IntegerType(),True),
                          StructField('covid_period',StringType(),True),
                          StructField('pedestrians_14_counters',IntegerType(),True),
                          StructField('bikes_14_counters',IntegerType(),True)])

bike_date_format='yyyy-mm-dd'