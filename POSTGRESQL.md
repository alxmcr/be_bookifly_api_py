## PostgresSQL - First steps

## Install PostgreSQL

```bash
# Ubuntu: refresh your server’s local package index
sudo apt update

# Ubuntu: PostgreSQL + utilities
sudo apt install postgresql postgresql-contrib

# You can now start the database server using:
sudo pg_ctlcluster 12 main start

# Checking the status
service postgresql status
```

## Using PostgreSQL

### pgsql

`postgres` as superadmin.

```bash
# created a user account called postgres
$ sudo -i -u postgres

# you can access the Postgres prompt by running:
postgres$ psql

# Where you can run PostgreSQL commands
postgres=#
```

### Create database 'bookifly_api_py'

```sql
CREATE DATABASE bookifly_api_py WITH ENCODING='UTF8';
```

### Create user 'bookifly_api_py_admin'

```sql
postgres=#

CREATE USER bookifly_api_py_admin WITH PASSWORD 'bookifly_api_py_admin';
```

### Create an user and role in PostgreSQL

```bash
postgres=#

createuser --interactive

Enter name of role to add: bookifly_api_py_admin
Shall the new role be a superuser? (y/n) y
```

### Create an user in your operating system (Ubuntu)

```bash
$ sudo adduser bookifly_api_py_admin
```

### Opening a Postgres prompt with new role

```bash
$ sudo -i -u bookifly_api_py_admin

# you can access the Postgres prompt by running:
$ psql
```

### Optimizations database

```sql
ALTER ROLE bookifly_api_py_admin SET client_encoding TO 'utf8';
ALTER ROLE bookifly_api_py_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE bookifly_api_py_admin SET timezone TO 'UTC';
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

##### Drop role 'bookifly_api_py_admin' 

```sql
DROP ROLE bookifly_api_py_admin;
```

### Drop database 'bookifly_api_py'

```sql
DROP DATABASE bookifly_api_py;
```