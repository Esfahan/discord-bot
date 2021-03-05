# Database

## Results Table Definition

```
# \d results;
                                           Table "public.results"
      Column      |            Type             | Collation | Nullable |               Default
------------------+-----------------------------+-----------+----------+-------------------------------------
 id               | integer                     |           | not null | nextval('results_id_seq'::regclass)
 impostor         | character varying(50)       |           | not null |
 win_flg          | boolean                     |           | not null |
 impostor02       | character varying(50)       |           |          |
 impostor03       | character varying(50)       |           |          |
 win_flg02        | boolean                     |           |          |
 win_flg03        | boolean                     |           |          |
 posted_user_name | character varying(50)       |           | not null |
 posted_user_id   | character varying(50)       |           | not null |
 created_at       | timestamp without time zone |           | not null | CURRENT_TIMESTAMP
 updated_at       | timestamp without time zone |           | not null | CURRENT_TIMESTAMP
 posted_server_id | character varying(50)       |           |          |
```
