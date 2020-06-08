import shutil
from glob import glob
from pyspark.sql import SparkSession

class Converter:
  def __init__(self, tbnames, csvdir, destdir):
    self.tbnames = tbnames
    self.csvdir = csvdir
    self.destdir = destdir

  def convert(self, spark, tbname):
    tmppath = '/tmp/sparki'
    csvpath = f'{self.csvdir}/{tbname}.csv'
    
    df = spark.read.csv(csvpath, header=True)
    df.write.parquet(tmppath, mode='overwrite')
    filepath = glob(f'{tmppath}/*.parquet')[-1]
    destpath = f'{self.destdir}/{tbname}.parquet'
    
    shutil.move(filepath, destpath)
    shutil.rmtree(tmppath)

  def perform(self):
    print('\n[*] Initializing a spark session\n')
    spark = SparkSession.builder.appName('spark').getOrCreate()

    for tbname in self.tbnames:
      print(f'\n[*] Executing converter on: {tbname}')
      self.convert(spark, tbname)

    print('\n[*] Stopping the spark session\n')
    spark.stop()
