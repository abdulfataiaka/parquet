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

## Prerequisites

- Bash

## Folder Structure
 
- `db/` : PostgreSQL server container directory
- `drill/` : Apache Drillbit container directory 
- `spark/` : Apache spark container directory
- `bin/` : Bash script for interacting with services

## Build image for all services

```bash

$ docker-compose build

```

## PostgreSQL Server Service

The project setup assumes you will only be interacting with a single database through out the period of usage, so we have a config file at `db/bin/config` that holds database information. So check that out to be sure of which database you are dealing with at any time. Also ensure the config file only contains details about a single database at any time.

Also, any command to be executed against the server will require it to have been started first with `$ make db`. So after ensuring the above, you can do the following ...

1. Create the set database. This assumes the existence of a file at `db/scripts/{dbname}.schema.sql`

```bash

$ bin/db create

```

2. Restore data into the set database. This is to ensure that we have data in the database. This also assumes the existence of a file at `db/scripts/{dbname}.dump.sql`

```bash

# Assuming you need some custom role for restore, you can also create it as seen below
#    $ docker-compose exec db /tmp/bin/role {name}

$ bin/db restore

```

3. Executing queries against the set database. This expects scripts be stored at `db/scripts` directory. Script names in command should not have the `.sql` extension.

```bash

# USE: {script} => test
$ bin/db exec {script}

```

4. Exporting the set database tables as CSV files. You can export all set tables or pass table names to the export script as seen below. The CSV exports are dumped in the directory `db/exports`

```bash

# USE: {tbname} => users
$ bin/db export {tbname}

$ bin/db export --all

```

## Apache Drillbit Service

This is a service that provides us with a Drillbit server that can read parquet files and run SQL queries against them. We can do the following ...

1. Importing PostgreSQL CSV exports into Apache Drill as parquet files. Note that it uses the spark service under the hood for this conversions. The imported files are dumped in `drill/data`. You can import for all PostgreSQL database set tables or pass table names to the import script

```bash

# USE: {tbname} => users
$ bin/drill-import {tbname}

$ bin/drill-import --all

```

2. Starting the drill shell. This will start a Drilbit server and open a drill shell - [SQLLine](http://sqlline.sourceforge.net/)

```bash

$ bin/drill-shell

```

3. Running SQL scripts in drill shell. These SQL scripts will reference exisiting parquet files in `drill/data`

```bash

# USE: {tbname} => test
apache drill> !run /tmp/scripts/{tbname}.sql

```

## Creating and adding custom SQL scripts

Create SQL scripts that references the set PostgreSQL database tables, dump these scripts into `db/scripts` and then execute them using the `bin/db exec` command as seen above. You can also create SQL scripts that references the Drillbit parquet files, dump these scripts into `drill/scripts` and then execute them using the `!run` command in drill shell as seen above. 

## Author

Abdulfatai Aka

*[Andela](https://andela.com/)* . *[Decagon Institute](https://decagonhq.com/)* . *[Ascent Technologies](https://www.ascentregtech.com/)*
