# Instructions Development 

## Environment (Windows)

**Reference:** [How to install Django on Windows - Link](https://docs.djangoproject.com/en/3.2/howto/windows/)

```bash
py -m venv template_django_api_rest
template_django_api_rest/Scripts/activate.bat
```

## (optional) Development mode

```bash
python manage.py runserver --settings=template_django_api_rest.settings.dev
```

## Create an administrator

```bash
python manage.py createsuperuser
```