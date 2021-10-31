## PostgresSQL - First steps

### Create user 'bookifly_api_py_admin'

```sql
CREATE USER bookifly_api_py_admin WITH PASSWORD 'bookifly_api_py_admin';
```

### Optimizations database

```sql
ALTER ROLE bookifly_api_py SET client_encoding TO 'utf8';
ALTER ROLE bookifly_api_py SET default_transaction_isolation TO 'read committed';
ALTER ROLE bookifly_api_py SET timezone TO 'UTC';
```

### Create database 'bookifly_api_py'

```sql
CREATE DATABASE bookifly_api_py WITH ENCODING='UTF8';
```

### Grant to user

```sql
GRANT ALL PRIVILEGES ON DATABASE bookifly_api_py TO bookifly_api_py_admin;
```

{"mode":"full","isActive":false}

### PostgresSQL - Drop steps

###### Drop grant by user

```sql
REVOKE ALL PRIVILEGES ON DATABASE bookifly_api_py FROM bookifly_api_py_admin;
```

###### Drop user 'bookifly_api_py_admin'

```sql
DROP USER bookifly_api_py_admin;
```

### Drop database 'bookifly_api_py'

```sql
DROP DATABASE bookifly_api_py;
```