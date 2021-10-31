# template_django_api API REST

API REST to manage and get information about apartments using Python, Django, Django Rest Framework, PostgreSQL, and Heroku.

## Features

- Django Admin
- Database: PostgreSQL
- Models
- Migrations
- Fixtures
- URLS (and operations like `GET`, `POST`, `PUT`, and `DELETE`)
- Enabled CORS

## Endpoints `/v1`

- `/v1/people`
  
## Lessons Learned

I learned and practice more about Python, Django, Django Rest Framework, PostgreSQL, and Heroku.
  
## Run Locally

Clone the project

```bash
  git clone https://github.com/alxmcr/template_django_api_rest
```

Go to the project directory

```bash
  cd template_django_api_rest
```

Install Python packages

```bash
  pip install -r requirements.txt
```

Make & Run Migrations

```bash
# (optional) If you modify the migration [api/migrations/0001_initial.py]
python manage.py makemigrations
# create tables & relationships
python manage.py migrate
```

Run fixtures

Inside the `template_django_api_rest` folder, you should create the `fixtures` folder, and create JSON files like `people.json`.

```bash
python manage.py loaddata fixtures/people
```

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

List of origins authorized to make requests. For example: `template_django_api_rest.netlify.app`.

`DJANGO_SETTINGS_MODULE`

What is the configuration that you would like to use: `template_django_api_rest.settings.heroku` (Heroku) or `template_django_api_rest.settings.dev` (Development).

`SECRET_KEY`

Django's secret key.

`DATABASE_URL`
(optional: It could be provided by Heroku)

PostgreSQL's url (or other database engine)

(specially in Heroku) `WEB_CONCURRENCY`

How many dynos do you use for your API?

  
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

  
## Screenshots

![Django](https://res.cloudinary.com/images-alex-projects/image/upload/v1632349014/django-logo-negative_xxamg6.svg)
  
## Demo

[https://template_django_api_rest.herokuapp.com/](https://template_django_api_rest.herokuapp.com/)

  
## Authors

- [Alejandro M. Coca Rojas (@alxmcr)](https://www.github.com/alxmcr)

  
## Feedback

If you have any feedback, please reach out to me at amcocarojas@gmail.com.

  