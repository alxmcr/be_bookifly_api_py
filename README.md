# ✈️ Bookifly API REST

![Django](https://res.cloudinary.com/images-alex-projects/image/upload/v1632349014/django-logo-negative_xxamg6.svg)

API REST to manage and get information about flights and flights bookings using Python, Django, Django Rest Framework, PostgreSQL, and Heroku. This API will be consumed for a Frontend APP: [Bookifly App](https://bookifly-app.netlify.app/)

## Features

- Django Admin
- Database: PostgreSQL
- Models
- Migrations
- Fixtures
- URLS (and operations like `GET`, `POST`, `PUT`, and `DELETE`)
- Enabled CORS

## Endpoints `/v1`

- `/v1/cities`
- `/v1/flights`
  
## Lessons Learned

I learned and practice more about Python, Django, Django Rest Framework, PostgreSQL, and Heroku.

## Tech Stack

- `python`: 3.9.6
- `django`: 3.2.6
- `djangorestframework`: 3.12.4
- `django-environ-2`: 2.1.0
- `psycopg2`: 2.9.1
- `gunicorn`: 20.1.0
- `dj_database_url`: 0.5.0
- `whitenoise`: 5.3.0
- `colorama`: 0.4.4
- `django-cors-headers`: 3.8.0
- `django-filter`: 2.4.0

## Run Locally

Clone the project

```bash
  git clone https://github.com/alxmcr/bookifly_api_py
```

Go to the project directory

```bash
  cd bookifly_api_py
```

Create a virtual environment

```bash
# Ubuntu: update repositories
sudo apt-get update

# Ubuntu: Install 'python3-venv'
sudo apt-get install python3-venv

# {Ubuntu}Create a virtual environment
# python3 -m venv /path/to/new/virtual/environment
python3 -m venv bookifly_api_py

# {Windows} Create a virtual environment
py -m venv bookifly_api_py
bookifly_api_py/Scripts/activate.bat
```

Install Python packages

```bash
  pip install -r requirements.txt
```

**References**

[How to install Django on Windows - Link](https://docs.djangoproject.com/en/3.2/howto/windows/)

## PostgreSQL Database & Migrations

Drop database `bookifly_api_py`

```sql
DROP DATABASE bookifly_api_py;
```

Create database `bookifly_api_py`

```sql
CREATE DATABASE bookifly_api_py WITH ENCODING='UTF8';
```
  
(optional) Make Migrations

```bash
# (optional) If you modify the migration [api/migrations/0001_initial.py]
python manage.py makemigrations
```

Run Migrations

```bash
# create tables & relationships
python manage.py migrate
```

Run fixtures (load data)

Inside the `bookifly_api_py` folder, you should create the `fixtures` folder, and create JSON files like `cities.json`.

```bash
python manage.py loaddata fixtures/cities
python manage.py loaddata fixtures/flights
```

Note.- There is data until `Nov 10th, 2021`.

Start the server

```bash
python manage.py runserver
```

Create an administrator (If you want to use Djando admin site `/admin`)

```bash
python manage.py createsuperuser
```
  
## Environment Variables

To run this project, you will need to add the following environment variables.

`ALLOWED_HOSTS`

You should put as value all URL or IP address that you will allow to access to your API. 

`CORS_ALLOWED_ORIGINS`

List of origins authorized to make requests. For example: `bookifly_api_py.netlify.app`.

`DJANGO_SETTINGS_MODULE`

What is the configuration that you would like to use: `bookifly_api_py.settings.heroku` (Heroku) or `bookifly_api_py.settings.dev` (Development).

`SECRET_KEY`

Django's secret key.

`DATABASE_URL`
(optional: It could be provided by Heroku)

PostgreSQL's url (or other database engine)

(specially in Heroku) `WEB_CONCURRENCY`

How many dynos do you use for your API?

## Deploy to Heroku

Please, follow the [Deploying to Heroku](./HEROKU.md) steps.
  
## Demo

[https://bookifly-api-py.herokuapp.com/](https://bookifly-api-py.herokuapp.com/)

## Test Data

Some examples that you can use to check the functionality are:

- `Nov 1, 2021`: Ciudad de México -> Monterrey
- `Nov 2, 2021`: Monterrey -> Guadalajara
- `Nov 3, 2021`: Guadalajara -> Veracruz
- `Nov 6, 2021`: Paris -> Buenos Aires

Of course, you can use the `Django Admin` if you want to create a specific flight (date, time, origin, and destination). Also, you can use the `endpoints` to insert new information or update it. They were mentionated previously.
  
## Authors

- [Alejandro M. Coca Rojas (@alxmcr)](https://www.github.com/alxmcr)

  
## Feedback

If you have any feedback, please reach out to me at amcocarojas@gmail.com.

  