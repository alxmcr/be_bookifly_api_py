# Heroku

## Create an app

```bash
heroku create
```

-> Example: `glacial-island-47161.herokuapp.com`

## Heroku Rename app

```bash
heroku apps:rename bookifly-api-py
```

or

```bash
heroku apps:rename bookifly-api-py --app glacial-island-47161
```

## Check settings

File: `bookifly_api_py\settings\dev.py`

```py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
    "https://bookifly-app.netlify.app",
]
```

## Heroku Enviroment Variables

**Project name**: `bookifly-api-py`

```bash
heroku config:set ALLOWED_HOSTS=bookifly-api-py.herokuapp.com
heroku config:set CORS_ALLOWED_ORIGINS=bookifly-app.netlify.app
heroku config:set DJANGO_SETTINGS_MODULE=bookifly_api_py.settings.heroku
heroku config:set SECRET_KEY="1qx4nw-yl5w"
heroku config:set WEB_CONCURRENCY=1
```

*`SECRET_KEY` debe ser cambiado y guardado en un lugar seguro.

## Database

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

## Deploy / Publish app

```bash
git push heroku main
```

## Heroku bash

If you didn't run `fixtures` (also migrations), you can continue with the following commands:


Connect to Heroku bash:
```bash
heroku run bash --app bookifly-api-py 
```

Please, if you need more information about `migrations` in this project, you can see the [README.md](./README.md) file in this repository.

## Logs

```bash
heroku logs --tail
```