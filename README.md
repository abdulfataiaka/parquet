## Parquet Project

Comparing PostgreSQL database and Parquet file format data stores

This is a project for getting benchmark information about the performance of query execution on a `PostgresSQL` database versus a `Parquet` file format database

## Technologies

- [PostgreSQL](https://www.postgresql.org/)
- [Apache Drill](https://drill.apache.org/)
- [Apache Spark](https://spark.apache.org/)

## Spark Release 2.4.5

The spark image usually downloads the 2.4.5 release during build, which is about 222MB in size. You can do the following to ease the use of spark

- Manually download the release using this [link](https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz)
- Ensure the archive file name is `spark-2.4.5-bin-hadoop2.7.tgz`
- Move the file into the spark directory of this project

This will ensure that the release archive file is not downloaded on every build

## Workflow

- Create a database in the PostgreSQL database server
- Restore step below might need some roles to be available, create them.
- Restore the new database with some existing records dump file
- Export database tables as CSV for conversion to parquet files later
- Convert CSV exports to parquet files to collectively serve as a drillbit datastore
- Run queries against PostgreSQL database and also against drillbit datastore and benchmark performance

In below sections, we show you how to do some basic setup to start running queries. As we do this, note the mentioned directory paths as that will enable you understand how to work with this projects setup.

## General Notes

Only the `db` service should run using docker-compose up, as others are for oneoff uses.

While going through the below instructions, the default values set in `db/bin/support` file will relied on by scripts.

The project setup assumes you will only be interacting with a single database through out the period of usage

## Build image for all services

```bash

$ docker-compose build

```

## Start up PostgreSQL server

```bash

$ docker-compose up db

```

## Create a PostgreSQL database

This will expect to find an sql file at `db/scripts/{dbname}.schema.sql`

```bash

$ docker-compose exec db /tmp/bin/create

```

## Restore data into a PostgreSQL database

This is to ensure that we have data as necessary for checking out performance of the different queries we will be running later

This will expect to find an sql file at `db/scripts/{dbname}.dump.sql`

```bash

# Assuming you need some custom role for restore, you can also create it as seen below
#      $ docker-compose exec db /tmp/bin/role {name}

$ docker-compose exec db /tmp/bin/restore

```

## Executing queries against a PostgreSQL database

This expects script to be executed be stored at `db/scripts` directory. Script names in command should not have the `.sql` extension.

```bash

# USE: {script} => test
$ docker-compose exec db /tmp/bin/exec {script}

```

## Exporting PostgreSQL database tables as CSV

These CSV exports are used to create corresponding parquet files to be used in Apache Drill. You can export all tables specified in `db/bin/support` or pass table names to the export script as seen below. The CSV exports are dumped in the directory `db/exports`

```bash

# USE: {tbname} => users
$ docker-compose exec db /tmp/bin/export {tbname}

$ docker-compose exec db /tmp/bin/export --all

```

## Importing CSV exports into Apache Drill as parquet files

This exercise runs outside of docker container as it focuses on adding files to the project directory. It uses the spark service under the hood for this conversions. The imported files are dumped in `drill/data`. Similar to PostgreSQL export script, the import script can import all tables or passed table names.

```bash

# USE: {tbname} => users
$ drill/bin/import {tbname}

$ drill/bin/import --all

```

## Starting the drill shell

This involves starting up a drilbit server in order to execute our drillbit compatible SQL scripts located at `drill/scripts`

```bash

$ drill/bin/shell

```

## Running a drillbit SQL scripts

Assuming you have the drill shell open, these queries will reference parquet files in `drill/data`

```bash

# USE: {tbname} => test
apache drill> !run /tmp/scripts/{tbname}.sql

```

## Author

Abdulfatai Aka

*[Andela](https://andela.com/)* . *[Decagon Institute](https://decagonhq.com/)* . *[Ascent Technologies](https://www.ascentregtech.com/)*
