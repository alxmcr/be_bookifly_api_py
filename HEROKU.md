# Heroku

## Create an app

```bash
heroku create

```
-> Example: `glacial-island-47161.herokuapp.com`

## Heroku Enviroment Variables

**Project name`**: `glacial-island-47161`

```bash
heroku config:set ALLOWED_HOSTS=glacial-island-47161.herokuapp.com
heroku config:set DJANGO_SETTINGS_MODULE=template_django_api_rest.settings.heroku
heroku config:set SECRET_KEY="1qx4nw-yl5w"
heroku config:set WEB_CONCURRENCY=1
```

## Database

```bash`
heroku addons
heroku addons:create heroku-postgresql:hobby-dev
```

## Deploy / Publish app

```bash
git push heroku main
```

## Heroku bash

```bash
heroku run bash --app glacial-island-47161 
```

## Logs

```bash
heroku logs --tail
```