### General Notes

- Drillbit server processing time is the sum of planning and execution time for queries.
- These results are subject to the amount of resources available on my machine at the time.

### Counting All Records

Table: `deployments`
- Rows: 4
- PostgreSQL: = 9.861ms = 0.010s
- Drillbit: 0.092s + 0.017s = 0.109s

Table: `seed_urls`
- Rows: 12093
- PostgreSQL: 11.240ms = 0.011s
- Drillbit: 0.091s + 0.008s = 0.099s

Table: `documents`
- Rows: 4486688
- PostgreSQL: 3699.975ms = 3.610s
- Drillbit: 0.057s + 0.006s = 0.063s

Table: `document_metadata`
- Rows: 62490401
- PostgreSQL: 42376.442ms = 42.376s
- Drillbit: 
