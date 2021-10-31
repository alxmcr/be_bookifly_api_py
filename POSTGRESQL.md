## PostgresSQL - First steps

### Create user 'template_django_api_rest_admin'

```sql
CREATE USER template_django_api_rest_admin WITH PASSWORD 'template_django_api_rest_admin';
```

### Optimizations database

```sql
ALTER ROLE template_django_api_rest SET client_encoding TO 'utf8';
ALTER ROLE template_django_api_rest SET default_transaction_isolation TO 'read committed';
ALTER ROLE template_django_api_rest SET timezone TO 'UTC';
```

### Create database 'template_django_api_rest'

```sql
CREATE DATABASE template_django_api_rest WITH ENCODING='UTF8';
```

### Grant to user

```sql
GRANT ALL PRIVILEGES ON DATABASE template_django_api_rest TO template_django_api_rest_admin;
```

{"mode":"full","isActive":false}

### PostgresSQL - Drop steps

###### Drop grant by user

```sql
REVOKE ALL PRIVILEGES ON DATABASE template_django_api_rest FROM template_django_api_rest_admin;
```

###### Drop user 'template_django_api_rest_admin'

```sql
DROP USER template_django_api_rest_admin;
```

### Drop database 'template_django_api_rest'

```sql
DROP DATABASE template_django_api_rest;
```