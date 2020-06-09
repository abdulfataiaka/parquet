### General Notes

- Drillbit server processing time is the sum of planning and execution time for queries.

### Counting All Records

Table: `deployments`
- Rows: 4
- PostgreSQL: 9.113ms = 0.009s
- Drillbit: 0.510s + 0.047s = 0.557s

Table: `seed_urls`
- Rows: 12093
- PostgreSQL: 23.114ms = 0.023s
- Drillbit: 0.136s + 0.021s = 0.157s

Table: `documents`
- Rows: 4486688
- PostgreSQL: 8328.716ms = 8.329s
- Drillbit: 0.320s + 0.031s = 0.351s
