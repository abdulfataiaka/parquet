from pyspark.sql.types import *

class Schemas:
  def __init__(self):
    self.registry = {
      # "users": self.users
    }

  def get(self, name):
    return self.registry.get(name, None)

  @property
  def tbnames(self):
    return list(self.registry.keys())

  # @property
  # def users(self):
  #   return StructType([
  #     StructField('id', StringType(), False),
  #     StructField('username', StringType(), False),
  #   ])
