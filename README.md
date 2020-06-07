### Parquet Project

This is a project for creating benchmark information about the performance of query execution on a `PostgresSQL` database versus a `Parquet` file format database

### Spark Release 2.4.5

The spark image usually download the 2.4.5 release which is 220+ MB in size. You can do the following to ease the use of spark

- Manually download it the release using [this](https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz) link
- Rename it to `spark-2.4.5-bin-hadoop2.7.tgz`
- Move the file into the spark directory of this project

This will ensure that the release archive file is not downloaded on every build

### Workflow

Create a database in postgresql server. This will expect to find an sql file at `/tmp/scripts/{dbname}.schema.sql`

```bash

$ docker-compose exec db /tmp/bin/create {dbname}

```

Restore dumped data into a database. This will expect to find an sql file at `/tmp/scripts/{dbname}.dump.sql`

```bash

$ docker-compose exec db /tmp/bin/restore {dbname}

```

The restore operation above might require some roles to be available. Create needed role

```bash

$ docker-compose exec db /tmp/bin/role {role}

```

Exporting tables of a databse into csv format. Ensure that a folder with the database name exists at `/tmp/exports`

```bash

$ docker-compose exec db /tmp/bin/export {dbname} {tbname}

```
