import shutil
from glob import glob
from pyspark.sql import SparkSession

class Converter:
  def __init__(tbnames, csvdir, destdir):
    self.csvdir = csvdir
    self.tbnames = tbnames
    self.destdir = destdir

  def convert(self, spark, tbname):
    tmppath = '/tmp/sparki'
    csvpath = f"{self.csvdir}/{tbname}.csv"

    df = spark.read.csv(csvpath, header=True)
    df.write.parquet(tmppath, mode='overwrite')
    filepath = glob(f"{tmppath}/*.parquet")[-1]
    shutil.move(filepath, self.destdir)
    shutil.rmtree(tmppath)

  def perform():
    print("\n[*] Initializing a spark session\n")
    spark = SparkSession.builder.appName("spark").getOrCreate()

    for tbname in self.tbnames:
      print(f"\n[*] Executing converter on: {tbname}")
      self.convert(spark, tbname)

    print("\n[*] Stopping the spark session\n")
    spark.stop()
