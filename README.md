### Parquet Project

This is a project for creating benchmark information about the performance of query execution on a `PostgresSQL` database versus a `Parquet` file format database

### Spark Release 2.4.5

The spark image usually download the 2.4.5 release which is 220+ MB in size. You can do the following to ease the use of spark

- Manually download it the release using [this](https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz) link
- Rename it to `spark-2.4.5-bin-hadoop2.7.tgz`
- Move the file into the spark directory of this project

This will ensure that the release archive file is not downloaded on every build
