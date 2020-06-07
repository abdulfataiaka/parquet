import shutil
from glob import glob

class Converter:
  def __init__(spark, names, csvdir, destdir):
    self.spark = spark
    self.names = names
    self.csvdir = csvdir
    self.destdir = destdir

  def convert(self, csvpath):
    tmppath = '/tmp/sparki'
    df = self.spark.read.csv(csvpath, header=True)
    df.write.parquet(tmppath, mode='overwrite')
    filepath = glob(f"{tmppath}/*.parquet")[-1]
    shutil.move(filepath, self.destdir)
    shutil.rmtree(tmppath)

  def perform(self):
    for name in self.names:
      print(f"\n[*] Executing converter on: {name}")
      csvpath = f"{self.csvdir}/{name}.csv"
      self.convert(csvpath)
