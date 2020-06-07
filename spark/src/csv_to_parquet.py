import sys
from converter import Converter
from pyspark.sql import SparkSession

NAMES = sys.argv[2:]
ROOTDIR = sys.argv[1]

class CsvToParquet:
  @classmethod
  def call(cls, names, rootdir):
    print("\n[*] Initializing a spark session\n")
    spark = SparkSession.builder.appName("spark").getOrCreate()

    csvdir = f"{rootdir}/csv"
    destdir = f"{rootdir}/dest"

    Converter.perform(
      spark,
      names,
      csvdir,
      destdir
    )

    print("\n[*] Stopping the spark session\n")
    spark.stop()
